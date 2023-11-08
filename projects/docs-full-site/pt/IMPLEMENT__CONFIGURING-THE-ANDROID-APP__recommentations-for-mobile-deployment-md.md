---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/capture-app/recommendations-for-a-dhis2-mobile-deployment.md"
revision_date: "2021-04-21"
---

# Recomendações para uma implantação móvel DHIS 2 { #capture_app_recommendations }

Se você planeja implantar o aplicativo DHIS2 Android em campo, recomendamos fortemente que você leia as [Diretrizes de implementação para dispositivos móveis] (https://docs.dhis2.org/master/en/dhis2_android_implementation_guideline/about-this-guide.html) publicado pela UiO. Inclui capítulos sobre requisitos de tecnologia, aspectos de segurança e configuração e recomendações de teste e implementação. Abaixo você encontrará alguns aspectos-chave brevemente introduzidos. Recomendamos a leitura do documento estendido

## Especificações do dispositivo móvel { #capture_app_recommendations_mobile_specs }

O aplicativo Android é compatível e compatível com DHIS 2 versões 2.30 a 2.36. E não tem alterações significativas com 2.29.

Requer um dispositivo com Android v4.4 (não recomendado, mas compatível) ou superior. O mínimo recomendado para novos dispositivos: Android 7 ou superior.

Em [a seção específica das Diretrizes de implementação para dispositivos móveis] (https://docs.dhis2.org/master/en/dhis2_android_implementation_guideline/mobile-device-specifications.html) você encontrará recomendações para novas aquisições de dispositivos móveis para uma implantação do Dhis2 Android.

## Teste e pilotagem { #capture_app_recommendations_testing }

Se você planeja implantar o aplicativo DHIS 2 para Android em campo, primeiro deve fazer uma rodada completa de testes do aplicativo em sua própria configuração.

O aplicativo foi amplamente testado com os servidores de demonstração e, durante o teste Beta, também foi testado em algumas configurações reais. Sabemos, entretanto, que toda configuração de DHIS 2 é especial em muitos sentidos e pode causar inconsistências que não conseguimos identificar.

É altamente recomendável realizar um teste abrangente do aplicativo em seu próprio servidor antes de executá-lo.

## Como migrar para o Aplicativo Android de Captura { #capture_app_recommendations_migration }

Se você estiver pronto para implantar o novo aplicativo Android em campo e seus utilizadores já estiverem usando a Captura de eventos ou a Captura do rastreador, você deve seguir estas etapas:

1.  Sincronizar dados do aplicativo atual que você está usando

    > **Warning**
    >
    > Deleting the app without syncing can cause information loss.

2.  Baixe e instale o aplicativo DHIS 2 para Android
3.  Faça login usando suas credenciais e todos os dados serão sincronizados.
