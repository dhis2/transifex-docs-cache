---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/mdm/choosing-an-mdm.md"
revision_date: "2021-03-29"
---

# Escolhendo um MDM / EMM { #mdm_choosing }

Ao decidir qual solução MDM escolher, é importante definir qual conjunto de recursos será considerado necessário e quais são adequados para ter. Isso pode variar muito entre as implementações; no entanto, identificamos alguns recursos como obrigatórios na lista abaixo devido à natureza do DHIS2. Embora isso possa ser revisado dependendo da implementação, eles devem ser considerados como nossa recomendação.

Consulte o Anexo A - Gerenciamento de dispositivos móveis para obter mais detalhes.

Recursos necessários e seus motivos:

- Android como plataforma compatível:

  Isso pode parecer óbvio, mas algumas soluções de MDM são destinadas a outros tipos de dispositivos, como iOS ou Windows. No momento, o DHIS2 Android App só é compatível com dispositivos Android e oferece suporte a partir da versão 4.4 (não recomendado) e superior (recomendamos a partir da versão 7).

- Gerenciamento de distribuição de aplicativos:

  As implementações do DHIS2 precisam testar e treinar os usuários antes de lançar uma nova versão do aplicativo. Como a maioria das implementações instala o DHIS2 Android App da Google Play Store, quando uma atualização é publicada lá, os dispositivos podem ser atualizados sem que o projeto esteja pronto se não houver outro mecanismo para gerenciar as atualizações.

- Informação de dispositivo:

  As implementações DHIS2 precisam manter um inventário de seus dispositivos para solucionar problemas ou atualizar seus dispositivos. Todas as soluções MDM consideradas incluem este um recurso básico, mas está listado aqui apenas no caso de existir uma solução que não pode incluir isso.

- Aplicação de senha:

  Na maioria (senão em todas) das implementações DHIS2, as informações confidenciais são armazenadas no aplicativo. Portanto, impor uma política de senha no dispositivo pode impedir o acesso indesejado a esses dados.

      Observe que apesar do aplicativo DHIS2 Android permitir a possibilidade de definir uma senha para controle de acesso, porque as informações no dispositivo ainda não estão criptografadas (fevereiro de 2020), ainda podem ser extraídas por um invasor.

- Limpeza remota:

  Na maioria (senão em todas) as informações confidenciais das implementações DHIS2 são armazenadas no aplicativo. Se, por exemplo, um dispositivo for perdido ou roubado, garantir que ele possa ser apagado remotamente pode ajudar a prevenir o vazamento de dados confidenciais.

É bom ter recursos e seus motivos:

- Modo quiosque (também conhecido como modo de aplicativo único)

  Algumas implementações DHIS2 podem exigir que os dispositivos sejam bloqueados para um único aplicativo (DHIS2 Android Capture App) sem permitir que o usuário acesse qualquer outro aplicativo ou configurações. Uma política de quiosque conseguiria isso.

- Gerenciamento de telefone

  Em algumas implementações DHIS2, pode ser necessário usar dispositivos com cartões SIM para fornecer conexão de dados em uma rede móvel (2G-5G). Isso pode exigir que os dispositivos usem serviços de chamadas específicos para recarregar pacotes de dados ou limitar o suporte de chamadas, etc.

- Restrições de aplicativos / configurações

  Algumas implementações DHIS2 podem exigir que os usuários sejam capazes de usar não apenas um, mas vários aplicativos (ou seja, um dispositivo que precisa ser usado para DHIS2 e captura de imagens).

- Gerenciamento de rede

  Algumas implementações DHIS2 podem exigir que os dispositivos não usem a rede de dados, ou se limitem a domínios específicos (firewall) ou sempre usem apenas redes sem fio específicas ou configurem dinamicamente as redes sem fio, etc.

- Gestão de usuários

  Algumas implementações DHIS2 podem exigir que os dispositivos sejam usados por vários usuários (até mesmo dois usuários DHIS2). A funcionalidade de gerenciamento de usuário pode aumentar o nível de segurança neste cenário, já que cada usuário pode ter diferentes códigos de acesso, permitindo contas de vários usuários para DHIS2 Android Capture App (atualmente sem suporte nativo), várias políticas de aplicativo por usuário, etc.

## Preço inicial e custos operacionais { #mdm_choosing_initial_price }

Um dos fatores críticos que os projetos enfrentarão ao decidir se desejam implementar um MDM é o preço inicial e os custos de operação. Um MDM pode trazer custos inesperados, por isso é recomendável avaliar a necessidade e incluir seus custos o mais cedo possível na definição do projeto e orçamento.

A maioria das soluções de MDM apresentadas nas seções a seguir incluem um custo operacional mensal ou anual que pode aumentar tremendamente o custo do projeto dependendo do número de dispositivos. Portanto, é aconselhável considerar algumas das seguintes dicas:

1. Se o projeto tiver capacidade para hospedar a solução MDM em seus servidores, geralmente apresentará uma opção melhor do que escolher uma solução incluindo hospedagem.
2. Alguns doadores podem impor a escolha de uma solução de MDM específica, se for o caso, certifique-se de que o orçamento seja alocado para fases futuras do projeto ou que o MDM possa ser usado gratuitamente (ou mais barato) com um conjunto limitado de opções.
3. A maioria das soluções oferece pacotes diferentes como modelo de preço, se a solução for principalmente (ou apenas) usada para gerenciar o aplicativo DHIS2 (instalação e atualização), o uso será mínimo, portanto, escolher a alternativa mais barata provavelmente será suficiente.
4. Devido à natureza da maioria dos projetos (saúde em países em desenvolvimento, ONGs, educação, etc.), muitos provedores de MDM provavelmente poderão oferecer um desconto. Negociar antes de escolher uma solução é altamente recomendável, pois ao escrever este documento muitos fornecedores demonstraram interesse e já ofereciam negócios melhores do que os anunciados em seus sites.

## BYOD / dispositivo corporativo { #mdm_choosing_byod }

Outro fator importante ao decidir qual MDM / EMM usar é considerar se a implantação incluirá uma política BYOD (Traga seu próprio dispositivo) ou se funcionará apenas com dispositivos corporativos. Isso pode ser um fator crítico, pois a maioria do MDM diferencia as políticas que podem ser aplicadas a esses dois tipos de dispositivos. Muitas implementações de DHIS2 são baseadas em dispositivos somente corporativos, mas em algumas implementações uma política de dispositivo BYOD-Corporate misto ou até mesmo uma política de dispositivo BYOD completa pode ser possível.

Uma configuração BYOD implica ter um MDM que permite um conjunto mínimo de políticas em conformidade com os recursos obrigatórios listados acima. Dependendo do MDM, isso pode exigir um perfil de trabalho onde o aplicativo DHIS2 deve ser instalado. Nessas implementações, o treinamento pode ser ainda mais importante para explicar as diferenças entre os perfis. Por exemplo, um usuário com o aplicativo DHIS2 instalado em seu perfil pessoal (bem como no perfil de trabalho) acrescentaria riscos de segurança de dados adicionais, porque quaisquer dados armazenados em seu perfil pessoal não poderiam ser apagados remotamente se o dispositivo fosse perdido ou roubado .

A configuração de um dispositivo corporativo implicará em ter todos os dispositivos sob um conjunto de políticas mais restritas (pode variar entre dispositivos / usuários / locais). Esta é a situação ideal do ponto de vista do gerenciamento de TI, mas afetará a flexibilidade e os custos.
