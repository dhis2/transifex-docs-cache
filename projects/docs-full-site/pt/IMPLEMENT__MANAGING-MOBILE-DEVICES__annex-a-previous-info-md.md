---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/mdm/A-a-previous-info.md"
revision_date: "2021-03-29"
---

# Annex A - Mobile Device Management (Previous information) {# mdm_previous }

> ** Nota **
>
> Essas são as mesmas informações que podem ser encontradas nas [Diretrizes de implementação do Android] (https://docs.dhis2.org/master/en/dhis2_android_implementation_guideline/scale-up.html#mobile-device-management). Em breve, essa seção será descontinuada em favor deste documento, mas é mantida aqui para fins históricos.

“_Mobile Device Management refere-se ao software usado para a administração de dispositivos móveis. Você precisará de um software MDM quando precisar oferecer suporte a centenas de dispositivos e for necessário controlar a distribuição do arquivo apk entre os dispositivos, fornecer suporte técnico e aplicar políticas institucionais. A maioria das opções é oferecida como serviços de taxa mensal. Alguns aplicativos gratuitos oferecem o modo quiosque, mas cobram uma taxa mensal para gerenciamento remoto básico_. ”

Os recursos desejáveis de um software MDM podem ser classificados como básicos e avançados. Aqui está uma lista dos recursos desejáveis:

- Recursos básicos:
  - Exigir uma senha de bloqueio de tela
  - Provisão de aplicativos autorizados
  - Bloqueie dispositivos e limpe as informações se eles forem perdidos ou roubados
  - Controlar a atualização do aplicativo Android
  - Aplicar políticas de backup
- Características avançadas:
  - Aplicar políticas de força de senha
  - Aplicar políticas de uso de rede
  - Rastrear localização do dispositivo
  - Restringir o acesso a configurações e recursos (exemplo - wi-fi / rede, captura de tela)

Ao decidir qual é o melhor software de MDM para suas necessidades, você deve tentar responder às seguintes perguntas:

- Quantos dispositivos eu preciso gerenciar?
- Com que frequência tenho acesso físico ao dispositivo?
- Quais recursos eu realmente preciso?
- Quais políticas devo implementar
- Será difícil instalar e manter
- Como isso afetará a experiência do usuário?
- Precisamos permitir BYO? (Traga seu próprio aparelho).
- Como isso afetará o dispositivo?
