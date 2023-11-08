---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/master/src/common/submitting-a-doc-fix.md"
revision_date: "2021-06-14"
---

# Odesílání rychlých oprav dokumentů { #submitting_doc_fixes }

U malých změn v dokumentu je skutečně velmi snadné pro kohokoli odesílat změny, aniž by prošel celým procesem založení problému v JIRA o DHIS 2. To lze provést přímo v [GitHub](https://github.com/dhis2/dhis2-docs) a nevyžaduje žádné znalosti git. _Vše, co potřebujete, je účet GitHub!_.

Tato část je zamýšlena jako návod k provedení jednoduchých změn.

## Kontrola překlepů { #typo-fix-walk-through }

V tomto scénáři čteme dokumentaci a najdeme překlep (slovo _manditory_ by mělo být _mand**a**tory_):

![Překlep v dokumentaci aplikace Capture](resources/images/doc_pr_001.png)

Toto je v kapitole „Používání aplikace Capture“ v uživatelské příručce DHIS 2. Chceme to napravit, takže ...

1.  Přihlásíme se na GitHub: https://github.com/dhis2/dhis2-docs

    Pokud nemáte účet, klikněte na odkaz  `Sign up`  na webu GitHub
    (public accounts are free) ![GitHub sign in](resources/images/doc_pr_001b.png)

2.  Nyní musíme najít kapitolu, kterou chceme změnit. Každá kapitola je jedním souborem v úložišti GitHub a na kapitoly se odkazuje ze souboru „INDEX“, který představuje celý dokument.

    Soubory indexů jsou zde: https://github.com/dhis2/dhis2-docs/tree/master/src/commonmark/en

    ![Indexové soubory dokumentace](resources/images/doc_pr_002.png)

    > You may notice the button near the top right that says "Branch: **master**". This indicates that we are looking at the documents for the master branch (i.e. the documentation for the very latest version of DHIS 2). If we wanted to edit the document for, say, version 2.29 instead, then we would use that button to select branch 2.29!  
    > (_2.29 is the earliest version supported in this markdown format_).

    a. V tomto případě je kapitola, kterou chceme, v Uživatelské příručce, takže otevřeme indexový soubor `dhis2_user_manual_en_INDEX.md`:

    > Pro správné zobrazení rejstříku vyberte režim  `Raw ` nebo  `Upravit`!

    ![Index souboru obsahu](resources/images/doc_pr_003.png)

    Tady vidíme, že na kapitolu „Používání aplikace Capture“ se odkazuje jako na `content/user/using-the-capture-app.md`

3.  Odkaz, který jsme našli výše, je cesta z aktuálního umístění, takže musíme přejít na: [https://github.com/dhis2/dhis2-docs/blob/master/src/commonmark/en/**content/user/using-the-capture-app.md**](https://github.com/dhis2/dhis2-docs/blob/master/src/commonmark/en/content/user/using-the-capture-app.md)

        ![Kapitola aplikace Capture](resources/images/doc_pr_004b.png)

4.  Odtud můžeme zvolit úpravu souboru (_ikona tužky_). Zobrazí se panel úprav:

        Here we have found and highlighted the offending word!
        ![Edit](resources/images/doc_pr_005.png)

        > Don't worry about the blue warning at the top that says we don't have
        write access to the file!

        We can make the change and preview it in the `Preview changes` tab if we want.
        Here is the preview:
        ![Preview](resources/images/doc_pr_006.png)

5.  Nakonec můžeme odeslat naši změnu jako _Pull Request_ (PR). We add a title for the change (and an _optional_ description) and click `Propose file change` ![Submit the change](resources/images/doc_pr_007.png)

    a. Vidíme souhrn našich změn a klikneme na `Create pull request`: ![Odeslat změnu](resources/images/doc_pr_008.png)

6.  Vše hotovo!

Nyní je v systému pull request, který může tým DHIS 2 snadno zkontrolovat a přijmout. ![Odeslat změnu](resources/images/doc_pr_009.png)

Po přijetí se změna objeví v dalším sestavení dokumentace!
