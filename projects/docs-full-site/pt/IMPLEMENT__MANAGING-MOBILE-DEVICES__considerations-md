---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/mdm/considerations.md"
revision_date: "2021-05-10"
---

# Considerations {# mdm_considerations }

Neste documento, os termos MDM e EMM serão usados alternadamente. Isso não é totalmente preciso, mas é feito para ajudar a simplificar o documento. Um MDM por si só não considera a implantação de aplicativos, enquanto um EMM envolve muito mais opções que não estão no escopo deste documento. Portanto, pode-se dizer que este documento cobre algo entre esses dois conceitos.

![MDM/EMM differences](resources/images/mdm-image7.png)

## Por que um MDM para DHIS2? {# mdm_considerations_why }

Gerenciamento de dispositivos móveis refere-se ao software usado para a administração de dispositivos móveis. Provavelmente, você desejará usar um software MDM quando precisar oferecer suporte a centenas de dispositivos e for necessário controlar a distribuição do aplicativo DHIS2 entre os dispositivos, fornecer suporte técnico e aplicar políticas institucionais.

Por exemplo, se você tiver um projeto em que 1000 dispositivos Android serão usados de forma distribuída (trabalhadores da comunidade) usando dados móveis para enviar as informações para o servidor DHIS2 central, ter um MDM pode ajudá-lo:

- Ser capaz de atualizar sempre que quiser o aplicativo DHIS2 Android quando uma nova versão for lançada. Observe que, por padrão, os dispositivos podem ser configurados para atualização automática ou você pode precisar solicitar a atualização manual do usuário. Um MDM oferece a possibilidade de escolher se deseja atualizar os dispositivos naquele ponto ou se prefere aguardar (por exemplo, até dar um treinamento explicando as novas opções do aplicativo).
- Localize e rastreie os dispositivos caso eles sejam perdidos ou limpe-os remotamente, caso possam conter informações confidenciais. Embora o aplicativo DHIS2 Android já inclua medidas de segurança se os telefones forem usados para coletar algumas fotos fora do aplicativo (por exemplo, de indivíduos, relatórios médicos, etc), pode representar um risco de privacidade / segurança.
- Desative o uso de dados móveis para qualquer aplicativo, exceto o aplicativo DHIS2 Android, ou desative a possibilidade de usar o Wireless Hotspot para que os pacotes de dados adquiridos pelo projeto sejam consumidos apenas para DHIS2.

## Como funciona um MDM? {# mdm_considerations_how_it_woks }

Esta seção explica resumidamente como um MDM / EMM funciona e como ele pode impactar a infraestrutura atual de uma implementação DHIS2.

Em uma implementação sem um MDM, os dispositivos se comunicam de maneira única e direta com o servidor DHIS2, conforme mostrado na imagem abaixo.

![Standard communication process between DHIS 2 Android APP and DHIS 2 server](resources/images/mdm-image9.png)

Adicionar um MDM impactará a infraestrutura, pois um novo servidor será adicionado. Esse servidor pode estar local (quando a solução oferece suporte) ou na nuvem. Embora não seja recomendado em casos realmente específicos (pequenas implantações ou restrições de orçamento), o servidor usado para hospedar DHIS2 também pode ser usado de forma que apenas um servidor seja necessário.

Adicionar um MDM também requer adicionar a posição de gerente de MDM, o que significa que uma pessoa precisa ser designada para configurar e gerenciar esse MDM. Este gerenciador implementa a configuração específica no servidor MDM e pode precisar configurar os dispositivos móveis.

![MDM is added to the infrastructure](resources/images/mdm-image12.png)

A configuração implementada no servidor MDM é recuperada pelos dispositivos, o que implica a aplicação de políticas específicas aos dispositivos que podem restringir a forma como o dispositivo pode ser usado. Também pode permitir rastreamento remoto ou limpeza do dispositivo, se necessário.

![Devices now communicate with two different servers: DHIS 2 and MDM](resources/images/mdm-image6.png)

A imagem abaixo apresenta essas etapas combinadas em um único gráfico.

![Communications in a DHIS 2 implementation with MDM](resources/images/mdm-image5.png)
