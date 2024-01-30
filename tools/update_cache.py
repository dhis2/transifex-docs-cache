
import datetime
import concurrent.futures
import time

from translayer import tx3
import os

#create an instance of a transifex organisation (pass organisation slug and transifex API token)
org = "hisp-uio"
tx_token = os.getenv("TX_TOKEN")

tx = tx3.tx(org,tx_token)


projects = ["docs-full-site","dhis2-single-page-docs"]

for p in projects:
    project = tx.project(p)

    # get project resources
    resources = project.resources()
    ls = project.language_stats()
    
    for l in project.languages():

        proj_lang_path = "projects/"+p+"/"+l.code
        cache_timestamp_file = proj_lang_path+"/.cache_timestamp"

        # ensure "projects/<project>" directory exists
        if not os.path.exists(proj_lang_path):
            os.makedirs(proj_lang_path)
        

        # default min date is current time minus 10 years
        now_date = datetime.datetime.now()
        min_date = now_date - datetime.timedelta(days=3650)

        # get the min date from the "last_update" file in the project directory (minus one day to give some overlap)
        if os.path.exists(cache_timestamp_file):
            with open(cache_timestamp_file) as f:
                min_date = datetime.datetime.strptime(f.readline().strip(),'%Y-%m-%dT%H:%M:%SZ') - datetime.timedelta(days=365)


        tic = time.perf_counter()

        # use multithreaded workers to pull the translations from transifex
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for r in resources:
                l_stats = r.language_stats(l.code)
                last_update = datetime.datetime.strptime(l_stats['last_update'], '%Y-%m-%dT%H:%M:%SZ')
                if last_update > min_date:
                    # print(r.name,r.slug,last_update)
                    if l_stats['untranslated_strings'] == 0:
                        # print(last_update,r.name,r.slug)
                        # pull the resource from transifex
                        path = proj_lang_path+"/"+r.slug
                        executor.submit(r.pull,l.code,path,"default")
            
        toc = time.perf_counter()
        print(f"Pulled files from transifex in {toc - tic:0.4f} seconds")

        # write the now date to the "last_update" file in the project directory
        with open(cache_timestamp_file, "w") as f:
            f.write(now_date.strftime('%Y-%m-%dT%H:%M:%SZ'))



