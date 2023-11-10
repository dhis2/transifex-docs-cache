---
edit_url: "https://github.com/dhis2/dhis2-docs/blob/2.34/src/commonmark/en/content/developer/dhis2-and-r-integration.md"
---

# Integração DHIS2 e R

<!--DHIS2-SECTION-ID:rsetup-->

## Introdução

<!--DHIS2-SECTION-ID:rsetup_intro-->

R é um ambiente de computação estatística de código aberto disponível gratuitamente. R
refere-se tanto à linguagem de programação de computador, quanto ao
software que pode ser usado para criar e executar scripts R. Há
[inúmeras fontes na web] (http://cran.r-project.org/) que descrevem
o extenso conjunto de recursos de R.

R é uma extensão natural do DHIS2, pois fornece dados estatísticos poderosos
rotinas, funções de manipulação de dados e ferramentas de visualização. Isto
capítulo irá descrever como configurar R e DHIS2 no mesmo servidor, e
irá fornecer um exemplo simples de como recuperar dados do DHIS2
banco de dados em um quadro de dados R e execute alguns cálculos básicos.

## Instalando R

<!--DHIS2-SECTION-ID:rsetup_install-->

Se estiver instalando R no mesmo servidor que DHIS, você deve considerar
usando a Rede Comprehensive R Archive (CRAN) para obter as últimas
distribuição de R. Tudo que precisa fazer é adicionar o seguinte like a
seu arquivo `/etc/apt/source.list`.

**deb\<your R mirror\>/bin/linux/ubuntu \ <your Ubuntu distribution\>**

Precisará substituir **\<your R mirror\>** por um da lista
disponível [aqui.] (http://cran.r-project.org/mirrors.html) Também
precisa substituir **\<your Ubuntu distribution\>** com o nome do
distribuição que você está usando.

Depois de fazer isso, invoque os seguintes comandos

    sudo apt-get update
    gpg --keyserver pgp.mit.edu --recv-keys 51716619E084DAB9
    gpg --armor --export 51716619E084DAB9 | apt-key add -
    sudo apt-get install r-base r-cran-dbi

Neste ponto, deve ter uma instalação R funcional em seu
máquina.

A seguir, vamos ver se tudo está funcionando simplesmente invocando `R` de
a linha de comando.

```
R version 3.4.4 (2018-03-15) -- "Someone to Lean On"
Copyright (C) 2018 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

>
```

## Usando ODBC para recuperar dados de DHIS2 em R

<!--DHIS2-SECTION-ID:rsetup_odbc-->

Neste exemplo, usaremos um conector ODBC para todo o sistema que será
usado para recuperar dados do banco de dados DHIS2. Há alguns
desvantagens dessa abordagem, pois o ODBC é mais lento do que outros métodos
e levanta algumas questões de segurança, fornecendo um sistema amplo
conector para todos os usuários. No entanto, é um método conveniente para fornecer um
conexão com vários usuários. O uso do pacote RODBC será
usado neste caso. Outras alternativas seriam o uso do
[RPostgreSQL] (http://dirk.eddelbuettel.com/code/rpostgresql.html)
pacote, que pode interagir diretamente por meio do driver PostgreSQL
descrito na próxima seção.

Supondo que já tenha instalado R a partir do procedimento anterior
secção. Invoque o seguinte comando para adicionar as bibliotecas necessárias para
este exemplo.

`apt-get install r-cran-rodbc r-cran-lattice odbc-postgresql`

Em seguida, precisamos configurar a conexão ODBC. Edite o arquivo para se adequar
sua situação local usando o seguinte modelo como um guia. Vamos
crie e edite um arquivo chamado odbc.ini

    [dhis2]
    Description         = DHIS2 Database
    Driver              = /usr/lib/odbc/psqlodbcw.so
    Trace               = No
    TraceFile           = /tmp/sql.log
    Database            = dhis2
    Servername          = 127.0.0.1
    UserName            = postgres
    Password            = SomethingSecure
    Port                = 5432
    Protocol            = 9.0
    ReadOnly            = Yes
    RowVersioning       = No
    ShowSystemTables    = No
    ShowOidColumn       = No
    FakeOidIndex        = No
    ConnSettings        =
    Debug = 0

Finalmente, precisamos instalar a conexão ODBC com `odbcinst -i -d -f
odbc.ini`

No prompt R, execute os seguintes comandos para se conectar ao
Banco de dados DHIS2.

    > library(RODBC)
    > channel<-odbcConnect("dhis2")#Note that the name must match the ODBC connector name
    > sqlTest<-c("SELECT dataelementid, name FROM dataelement LIMIT 10;")
    > sqlQuery(channel,sqlTest)
                                                                            name
    1   OPD First Attendances Under 5
    2   OPD First Attendances Over 5
    3   Deaths Anaemia Under 5 Years
    4   Deaths Clinical Case of Malaria Under 5 Years
    5   Inpatient discharges under 5
    6   Inpatient Under 5 Admissions
    7   Number ITNs
    8   OPD 1st Attendance Clinical Case of Malaria Under 5
    9  IP Discharge Clinical Case of Malaria Under 5 Years
    10 Deaths of malaria case provided with anti-malarial treatment 1 to 5 Years
    >

Parece que R é capaz de recuperar dados do banco de dados DHIS2.

Como um exemplo ilustrativo, digamos que nos pediram para calcular o
porcentagem relativa de OPD masculino e feminino com menos de 5 atendimentos para o
últimos doze meses. Primeiro, vamos criar uma consulta SQL que nos fornecerá
as informações básicas que serão
    requeridos.

    OPD<-sqlQuery(channel,"SELECT p.startdate, de.name as de, sum(dv.value::double precision)
     FROM datavalue dv
     INNER JOIN period p on dv.periodid = p.periodid
     INNER JOIN dataelement de on dv.dataelementid = de.dataelementid
     WHERE p.startdate >= '2011-01-01'
     and p.enddate <= '2011-12-31'
     and de.name ~*('Attendance OPD')
     GROUP BY p.startdate, de.name;")

Armazenamos o resultado da consulta SQL em um quadro de dados R chamado
"OPD". Vamos dar uma olhada na aparência dos dados.

``` 
> head(OPD)
   startdate                                 de    sum
1 2011-12-01   Attendance OPD <12 months female  42557
2 2011-02-01   Attendance OPD <12 months female 127485
3 2011-01-01   Attendance OPD 12-59 months male 200734
4 2011-04-01   Attendance OPD 12-59 months male 222649
5 2011-06-01   Attendance OPD 12-59 months male 168896
6 2011-03-01 Attendance OPD 12-59 months female 268141
> unique(OPD$de)
[1] Attendance OPD <12 months female   Attendance OPD 12-59 months male  
[3] Attendance OPD 12-59 months female Attendance OPD >5 years male      
[5] Attendance OPD <12 months male     Attendance OPD >5 years female    
6 Levels: Attendance OPD 12-59 months female ... Attendance OPD >5 years male
> 

```

Podemos ver que precisamos agregar os dois grupos de idade (\<12 meses
e 12-59 meses) em uma única variável, com base no gênero. Vamos
remodelar os dados em uma tabela tabulada para tornar mais fácil
visualize e calcule os resumos.

    >OPD.ct<-cast(OPD,startdate ~ de) 
    >colnames(OPD.ct)
    [1] "startdate"                          "Attendance OPD 12-59 months female"
    [3] "Attendance OPD 12-59 months male"   "Attendance OPD <12 months female"  
    [5] "Attendance OPD <12 months male"     "Attendance OPD >5 years female"    
    [7] "Attendance OPD >5 years male" 

Remodelamos os dados para que os elementos de dados sejam individuais
colunas. Parece que precisamos agregar o segundo e o quarto
colunas juntas para obter a frequência feminina de menores de 5 anos e, em seguida, o
terceira e quinta colunas para obter a frequência do sexo masculino com menos de 5 anos.
permite o subconjunto dos dados em um novo quadro de dados apenas para obter o necessário
informações e exibir os resultados.

    > OPD.ct$OPDUnder5Female<-OPD.ct[,2]+OPD.ct[,4]#Females
    > OPD.ct$OPDUnder5Male<-OPD.ct[,3]+OPD.ct[,5]#males
    > OPD.ct.summary<-OPD.ct[,c(1,8,9)]#new summary data frame
    >OPD.ct.summary$FemalePercent<-
    OPD.ct.summary$OPDUnder5Female/
    (OPD.ct.summary$OPDUnder5Female + OPD.ct.summary$OPDUnder5Male)*100#Females
    >OPD.ct.summary$MalePercent<-
    OPD.ct.summary$OPDUnder5Male/
    (OPD.ct.summary$OPDUnder5Female + OPD.ct.summary$OPDUnder5Male)*100#Males 

Claro, isso poderia ser feito com muito mais elegância, mas para o
propósito da ilustração, este código é bastante detalhado. Por fim, vamos
exibir as informações necessárias.

    > OPD.ct.summary[,c(1,4,5)]
        startdate FemalePercent MalePercent
    1  2011-01-01      51.13360    48.86640
    2  2011-02-01      51.49154    48.50846
    3  2011-03-01      51.55651    48.44349
    4  2011-04-01      51.19867    48.80133
    5  2011-05-01      51.29902    48.70098
    6  2011-06-01      51.66519    48.33481
    7  2011-07-01      51.68762    48.31238
    8  2011-08-01      51.49467    48.50533
    9  2011-09-01      51.20394    48.79606
    10 2011-10-01      51.34465    48.65535
    11 2011-11-01      51.42526    48.57474
    12 2011-12-01      50.68933    49.31067

Podemos ver que os atendimentos masculino e feminino são muito semelhantes para
cada mês do ano, com parentes de comparecimento aparentemente maior do sexo masculino
ao atendimento feminino no mês de dezembro.

Neste exemplo, mostramos como recuperar dados do banco de dados DHIS2
e manipular com alguns comandos R simples. O padrão básico para
usando DHIS2 e R juntos, será a recuperação de dados do DHIS2
banco de dados com uma consulta SQL em um quadro de dados R, seguido por qualquer
rotinas (análise estatística, plotagem, etc.) que podem ser necessárias.


## Mapeamento com R e PostgreSQL

<!--DHIS2-SECTION-ID:rsetup_maps-->

Um exemplo um pouco mais extenso, usará a biblioteca RPostgreSQL e
várias outras bibliotecas para produzir um mapa a partir das coordenadas armazenadas em
o banco de dados. Vamos definir algumas funções auxiliares para fornecer uma camada
de abstração, o que tornará o código R mais reutilizável.

``` 
#load some dependent libraries
 library(maps)
 library(maptools)
 library(ColorBrewer)
 library(ClassInt)
 library(RPostgreSQL)

#Define some helper functions

#Returns a dataframe from the connection for a valid statement
dfFromSQL<-function (con,sql){
    rs<-dbSendQuery(con,sql)
    result<-fetch(rs,n=-1)
    return(result)
}
#Returns a list of latitudes and
 longitudes from the orgunit table
dhisGetFacilityCoordinates<- function(con,levelLimit=4) {
sqlCoords<-paste("SELECT ou.organisationunitid, ou.name,
substring(ou.coordinates from E'(?=,?)-[0-9]+\\.[0-9]+')::double precision as latitude,
substring(ou.coordinates from E'[0-9\\.]+'):double precision as
 longitude FROM organisationunit ou where ou.organisationunitid
 in (SELECT DISTINCT idlevel",levelLimit, " from _orgunitstructure)
 and ou.featuretype = 'Point'
 ;",sep="")
 result<-dfFromSQL(con,sqlCoords)
 return(result)
 }

#Gets a dataframe of IndicatorValues,
# provided the name of the indicator,
# startdate, periodtype and level
dhisGetAggregatedIndicatorValues<-function(con,
indicatorName,
startdate,
periodtype="Yearly",
level=4)
{
  sql<-paste("SELECT organisationunitid,dv.value FROM aggregatedindicatorvalue dv
where dv.indicatorid  =
(SELECT indicatorid from indicator where name = \'",indicatorName,"\') and dv.level
 =", level,"and
 dv.periodid  = 
(SELECT periodid from period where 
startdate = \'",startdate,"\'
and periodtypeid = 
(SELECT periodtypeid from periodtype
 where name = \'",periodtype,"\'));",sep="")
   result<-dfFromSQL(con,sql)
 return(result)
 }

#Main function which handles the plotting.
#con is the database connection
#IndicatorName is the name of the Indicator
#StartDate is the startdate
#baselayer is the baselayer
plotIndicator<-function(con,
IndicatorName,
StartDate,
periodtype="Yearly",
level=4,baselayer) 
{
#First, get the desired indicator data
myDF<-dhisGetAggregatedIndicatorValues(con,
IndicatorName,StartDate,periodtype,level)
#Next, get the coordinates
coords<-dhisGetFacilityCoordinates(con,level)
#Merge the indicataors with the coordinates data frame
myDF<-merge(myDF,coords)
#We need to cast the new data fram to a spatial data
#frame in order to utilize plot
myDF<-SpatialPointsDataFrame(myDF[,
c("longitude","latitude")],myDF)
#Define some color scales
IndColors<-c("firebrick4","firebrick1","gold"
,"darkolivegreen1","darkgreen")
#Define the class breaks. In this case, we are going
#to use 6 quantiles
class<-classIntervals(myDF$value,n=6,style="quantile"
,pal=IndColors)
#Define a vector for the color codes to be used for the
#coloring of points by class
colCode<-findColours(class,IndColors)
#Go ahead and make the plot
myPlot<-plot.new()
#First, plot the base layer
plot(baselayer)
#Next, add the points data frame
points(myDF,col=colCode,pch=19)
#Add the indicator name to the title of the map
title(main=IndicatorName,sub=StartDate)
#Finally, return the plot from the function
return(myPlot) }

```

Até este ponto, definimos algumas funções para nos ajudar a fazer um
mapa. Precisamos obter as coordenadas armazenadas no banco de dados e mesclar
estes com o indicador que planejamos mapear. Em seguida, recuperamos os dados
a partir da tabela de indicadores agregados, crie um tipo especial de quadro de dados
(SpatialPointsDataFrame), aplique algum estilo a isso e, em seguida, crie
o enredo.

    #Agora definimos a coisa real a fazer
    #Vamos obter uma conexão com o banco de dados
    con <- dbConnect (PostgreSQL (), user = "dhis", senha = "SomethingSecure", dbname = "dhis")
    #Defina o nome do indicador para traçar
    MyIndicatorName <- "Presença total do OPD"
    MyPeriodType <- "Anual"
    #Isso deve corresponder ao nível onde as coordenadas são armazenadas
    MyLevel <-4
    #Dado a data de início e tipo de período, é o suficiente
    #para determinar o período
    MyStartDate <- "2010-01-01"
    #Obter alguns dados do distrito da Zâmbia no GADM
    #Isso vai ser usado como camada de fundo
    con <- url ("http://www.filefactory.com/file/c2a3898/n/ZMB_adm2_RData")
    print (load (con)) #salvo como objecto de gadm
    #Faça o mapa
    plotIndicator (con, MyIndicatorName, MyStartDate, MyPeriodType, MyLevel, gadm)

Os resultados da função plotIndicator são mostrados abaixo.

![](resources/images/r/OPDAttendance.png)

Neste exemplo, mostramos como usar a biblioteca RPostgreSQL e outros
bibliotecas auxiliares (Maptools, ColorBrewer) para criar um mapa simples a partir do
DHIS2 data mart.

## Usando R, DHIS2 e a API de visualização do Google

<!--DHIS2-SECTION-ID:rsetup_google_visualization_api-->

A API de visualização do Google fornece um conjunto muito rico de ferramentas para o
visualização de dados multidimensionais. Neste exemplo simples, iremos
mostre como criar um gráfico de movimento simples com o Google Visualization
API usando o pacote R "googleVis". Informações completas sobre o pacote podem
ser encontrado [aqui.] (http://code.google.com/p/google-motion-charts-with-r/).
O princípio básico, como nos outros exemplos, é obter alguns dados
do banco de dados DHIS2, e trazê-lo para R, execute alguns pequenos
alterações nos dados para torná-lo mais fácil de trabalhar e, em seguida, criar
o gráfico. Neste caso, vamos comparar os dados ANC1,2,3 ao longo do tempo e ver
como eles estão relacionados com um gráfico de movimento.

    #Carregue algumas bibliotecas
    biblioteca (RPostgreSQL)
    biblioteca (googleVis)
    biblioteca (remodelar)
    #Uma pequena função auxiliar para obter um quadro de dados de algum SQL
    dfFromSQL <-function (con, sql) {
        rs <-dbSendQuery (con, sql)
        resultado <-fetch (rs, n = -1)
        retorno (resultado)
    }

    # Obtenha uma conexão de banco de dados
    usuário <- "postgres"
    senha <- "postgres"
    host <- "127.0.0.1"
    porta <- "5432"
    dbname <- "dhis2_demo"
    con <- dbConnect (PostgreSQL (), usuário = usuário,
    senha = senha, host = host, porta = porta, dbname = dbname)
    # Vamos recuperar alguns dados ANC do banco de dados de demonstração
    sql <- "SELECT ou.shortname como província,
    i.nome abreviado como indicador,
    extrair (ano de p.startdate) como ano,
     um valor
    DE valor do indicador agregado a
    INNER JOIN organisationunit ou on a.organisationunitid = ou.organisationunitid
    Indicador INNER JOIN i em a.indicatorid = i.indicatorid
    INNER JOIN período p em a.periodid = p.periodid
    ONDE a.indicatorid IN
    (SELECIONE o ID do indicador DISTINCT no indicador onde o nome abreviado ~ * ('ANC [123] Cobertura'))
    E a.organisationunitid IN
     (SELECIONE DISTINCT idlevel2 de _orgunitstructure onde idlevel2 não é nulo)
    AND a.periodtypeid = (SELECT DISTINCT periodtypeid from periodtype onde name = 'Yearly') "
    #Armazene isso em um quadro de dados
    anc <-dfFromSQL (con, sql)
    # Altere essas algumas colunas para fatores para que a reformulação funcione mais facilmente

    anc $ province <-as.factor (anc $ province)
    anc $ indicador <-as.factor (anc $ indicador)
    # Precisamos da variável de tempo como numérica
    anc $ ano <-as.numeric (as.character (anc $ ano))
    #Precisa converter a tabela em um formato ligeiramente diferente
    anc <-cast (anc, província + ano ~ indicador)
    #Agora, crie o gráfico de movimento e plote-o
    M <-gvisMotionChart (anc, idvar = "província", timevar = "ano")
    plot (M)

O gráfico resultante é exibido abaixo.


![](resources/images/r/google_vis_col_chart.PNG)

Usando pacotes como [brew] (http://cran.r-project.org/package=brew) ou
[Rapache] (http://rapache.net), esses tipos de gráficos podem ser facilmente
integrado em sites externos. Uma versão totalmente funcional do
o gráfico mostrado acima pode ser acessado
[aqui.] (http://dhis2.net/R/google-motion-chart.html)

## Usando PL/R com DHIS2

<!--DHIS2-SECTION-ID:rsetup_plr-->

A linguagem procedural para R é uma extensão do núcleo do PostgreSQL
que permite que os dados sejam passados do banco de dados para R, onde
cálculos em R podem ser executados. Os dados podem então ser passados de volta para
o banco de dados para processamento posterior. Neste exemplo, criaremos um
função para calcular algumas estatísticas de resumo que não existem por
padrão em SQL usando R. Em seguida, criaremos uma visualização SQL em DHIS2 para
exibir os resultados. A vantagem de utilizar R neste contexto é
que não precisamos escrever nenhuma quantidade significativa de código para retornar
essas estatísticas de resumo, mas simplesmente utilizam as funções integradas de R
para fazer o trabalho por nós.

Primeiro, precisará instalar o [PL / R] (http://www.joeconway.com/plr/),
que é descrito em detalhes
[aqui.] (http://www.joeconway.com/plr/doc/plr-install.html). Segue
o exemplo do site PL / R, vamos criar algum agregado personalizado
funciona como detalhado
[aqui.] (http://www.joeconway.com/plr/doc/plr-aggregate-funcs.html) Nós
irá criar duas funções, para retornar a mediana e a assimetria de um
faixa de valores.

    CRIAR OU SUBSTITUIR FUNÇÃO r_median (_float8) retorna float como '
      mediana (arg1)
    'linguagem' plr ';

    CRIAR mediana AGREGADA (
      sfunc = plr_array_accum,
      basetype = float8,
      stype = _float8,
      finalfunc = r_median
    );

    CRIAR OU SUBSTITUIR A FUNÇÃO r_skewness (_float8) retorna float como '
      requer (e1071)
      skewness (arg1)
    'linguagem' plr ';

    CRIAR assimetria AGREGADA (
      sfunc = plr_array_accum,
      basetype = float8,
      stype = _float8,
      finalfunc = r_skewness
    );

A seguir, definiremos uma consulta SQL que será usada para recuperar os dois
novas funções de agregação (mediana e assimetria) que serão calculadas
usando R. Neste caso, vamos obter apenas um único indicador dos dados
mart a nível distrital e calcular os valores de resumo com base no
nome do distrito a que pertencem os valores. Esta consulta é muito
específico, mas pode ser facilmente adaptado ao seu próprio banco de dados.

    SELECT  ou.shortname,avg(dv.value),
    median(dv.value),skewness(dv.value) FROM aggregatedindicatorvalue dv
    INNER JOIN period p on p.periodid = dv.periodid
    INNER JOIN organisationunit ou on 
    dv.organisationunitid = ou.organisationunitid
    WHERE dv.indicatorid = 112670
    AND dv.level = 3
    AND dv.periodtypeid = 3
    AND p.startdate >='2009-01-01'
    GROUP BY ou.shortname;

Podemos então salvar essa consulta na forma de SQL View no DHIS2. Um recortado
versão dos resultados são mostrados abaixo.


![](resources/images/r/r_plr.PNG)

Neste exemplo simples, mostramos como usar PL/R com o DHIS2
banco de dados e interface da web para exibir algumas estatísticas resumidas usando R para
realizar os cálculos.

## Usando esta API da Web DHIS2 com R

<!--DHIS2-SECTION-ID:rsetup_web_api-->

DHIS2 tem uma API Web poderosa que pode ser usada para integrar aplicativos
juntos. Nesta secção, ilustraremos alguns exemplos triviais de
o uso da API da Web e como podemos recuperar dados e metadados para
use em R. A API da Web usa autenticação HTTP básica (conforme descrito em
a secção API da Web deste documento). Usando dois pacotes R "RCurl" e
"XML", poderemos trabalhar com a saída da API em R. No
primeiro exemplo, obteremos alguns metadados do banco de dados.

```
#We are going to need these two libraries
require(httr)
require(magrittr)
base.url<-"https://play.dhis2.org/dev/"
url<-paste0(base.url,"api/me")
username<-"admin"
password<-"district"
login<-GET(url,)

url<-paste0(base.url,"api/reportTables/KJFbpIymTAo/data.csv",authenticate(username,password))
mydata<-GET(url) %>% content(.,"text/csv")
head(mydata)
```

Aqui, mostramos como obter alguns dados agregados da demonstração DHIS2
banco de dados usando a API Web DHIS2.

No próximo exemplo de código, iremos recuperar alguns metadados, nomeadamente uma lista
de elementos de dados e seus identificadores exclusivos.

```

#Obtenha a lista de elementos de dados. Desative a paginação e obtenha apenas alguns atributos.
requer(httr)


username<-"admin"
password<-"district"
base.url<-"https://play.dhis2.org/dev/"

login<-function(username,password,base.url) {
url<-paste0(base.url,"api/me")
r<-GET(url,authenticate(username,password))
if(r$status == 200L) { print("Logged in successfully!")} else {print("Could not login")}
}

getDataElements<-function(base.url) {

url<-paste0(base.url,"api/dataElements?fields=id,name,shortName")
r<-content(GET(url,authenticate(username,password)),as="parsed")
do.call(rbind.data.frame,r$dataElements)
}

login(username,password,base.url)
data_elements<-getDataElements(base.url)
head(data_elements)
```

O objecto `data_elements` agora deve conter um quadro de dados de todos os elementos de dados no sistema.

```
                                         name          id
2   Accute Flaccid Paralysis (Deaths < 5 yrs) FTRrcoaog83
210   Acute Flaccid Paralysis (AFP) follow-up P3jJH5Tu5VC
3           Acute Flaccid Paralysis (AFP) new FQ2o8UBlcrS
4     Acute Flaccid Paralysis (AFP) referrals M62VHgYT2n0
5        Additional notes related to facility uF1DLnZNlWe
6                              Admission Date eMyVanycQSC
```
