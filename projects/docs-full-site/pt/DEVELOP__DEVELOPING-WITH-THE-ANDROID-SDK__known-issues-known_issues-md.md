---
edit_url: "https://github.com/dhis2/dhis2-android-sdk/edit/master/docs/content/developer/known-issues.md" 
---
# Problemas conhecidos  { #known_issues } 

<!--DHIS2-SECTION-ID:known_issues-->

## Conclusão do conjunto de dados { #data-set-completion } 

- No DHIS2 versão 2.33.0 e 2.33.1, se um conjunto de dados for marcado como incompleto no servidor, este valor não será atualizado no SDK. Nessas versões, a API não expôs informações suficientes para saber se o status estava completo ou incompleto.

