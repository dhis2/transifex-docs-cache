---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/compatibility-strategy.md" 
---
# Estratégia de compatibilidade de versão DHIS2  { #compatibility_strategy } 

<!--DHIS2-SECTION-ID:compatibility_strategy-->

O SDK garante compatibilidade com as três versões mais recentes do DHIS 2 (consulte [Compatibilidade] (# compatibilidade)). Caso o SDK ainda seja compatível com as versões DHIS2 anteriores e nenhum problema grave tenha sido detectado, a compatibilidade pode ser estendida para as versões anteriores.

Para evitar login acidental em instâncias DHIS 2 não suportadas, o SDK bloqueia conexões para versões que ainda não são suportadas ou que foram descontinuadas.

Em relação ao modelo de dados e compatibilidade, a abordagem principal é estender o modelo de dados para ser capaz de suportar todas as versões DHIS 2. Geralmente acontece que as novas versões do DHIS 2 introduzem funcionalidade extra e não removem a existente, portanto, oferecer suporte a uma nova versão do DHIS 2 geralmente significa usar o modelo de dados mais recente.

Como regra geral, o SDK tenta evitar alterações significativas em sua API e os novos recursos são opcionais para o usuário. Essa regra é seguida tanto quanto possível, mas há casos em que o suporte a APIs novas e antigas para evitar a quebra tem um custo muito alto. Nesse cenário, o **SDK pode apresentar alterações importantes para ser compatível com a nova versão DHIS 2**.

Aqui pode encontrar alguns exemplos de mudanças no SDK e o efeito no aplicativo.

## Exemplo: pequena mudança { #example-minor-change } 

Até a versão 2.30, o modelo de programa tinha um atributo booleano chamado "captureCoordinates". Este atributo indica se as coordenadas (ponto) devem ser armazenadas naquele programa. A partir de 2.30, este atributo foi substituído por "featureType" com 4 valores possíveis: NONE, POINT, POLYGON, MULTI_POLYGON.

*Mudanças no SDK:*

A partir de 2.30, o SDK usa o atributo "featureType". Se a versão do servidor for inferior a 2.30, o SDK mapeia o valor "captureCoordinates" para:

- falso - NENHUM
- verdadeiro - PONTO

*Mudanças no aplicativo:*

O aplicativo agora é forçado a usar "featureType". As modificações no código são bastante diretas.

## Exemplo: grande mudança { #example-major-change } 

A partir de 2.30, o modelo de relacionamento sofreu uma profunda refatoração para permitir relacionamentos entre evento, inscrição e trackedEntityInstances. O SDK adotou o modelo para 2.30 e expõe esse modelo ao aplicativo. Ao interagir com a API, o SDK traduz entre os dois modelos internamente.

*Mudanças no aplicativo:*

Essa mudança implica que o aplicativo deve adotar um modelo diferente e as mudanças não são tão simples.


