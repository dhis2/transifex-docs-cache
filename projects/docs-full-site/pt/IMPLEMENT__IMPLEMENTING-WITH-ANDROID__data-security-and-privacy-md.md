---
edit_url: "https://github.com/dhis2/dhis2-android-capture-app/blob/master/docs/src/commonmark/en/content/implementation-guide/data-security-and-privacy.md"
revision_date: "2021-03-29"
---

# Segurança e privacidade de dados { #implementation_guide_datasec }

Com o novo DHIS 2 Android Capture App, os usuários coletarão dados individuais no ponto de prestação do serviço, que é o nível mais baixo de captura direta de dados, pois envolve o beneficiário direto. A captura de dados dessa forma permite a análise upstream sem comprometer os detalhes, torna a análise downstream possível, reduz erros e permite a análise post hoc para responder às perguntas identificadas após a coleta de dados e o design do sistema. No entanto, os dados individuais trazem desafios adicionais para os sistemas de informação, incluindo considerações de segurança e privacidade, considerações de prontidão e capacidade, uma vez que os coletores de dados com menor conhecimento de TI são fornecidos com ferramentas digitais e complicações adicionais com relação a análise, armazenamento e capacidade de resposta do sistema.

Há um amplo consenso sobre a necessidade de fornecer uma prática abrangente de segurança de dados. Esta prática de segurança abrangente deve considerar não apenas _confidencialidade_ e _integridade, _ mas também _disponibilidade de dados_. A Harvard Humanitarian Initiative [declarou] (https://hhi.harvard.edu/publications/signal-code-ethical-obligations-humanitarian-information-activities) que a própria informação, incluindo sua geração, comunicação e recepção, é um serviço humanitário básico necessidade que deve receber proteção igual a outras necessidades tradicionais, como comida, água, abrigo e cuidados médicos. The Roadmap for Health Measurement Anccountability (MA4Health), [declarado] (https://www.healthdatacollaborative.org/fileadmin/uploads/hdc/Documents/the-roadmap-for-health-measurement-and-accountability.pdf) que “ A saúde pública e os cuidados clínicos não podem ser prestados de forma segura, com alta qualidade e com boa relação custo-benefício, sem trocas de dados e informações contínuas, sustentáveis e seguras em todos os níveis do sistema de saúde ”. Ainda assim, a captura e o armazenamento de dados de identificação pessoal apresentam risco e uma obrigação proporcional para práticas de privacidade rigorosas.

A Universidade de Oslo está comprometida com o seguinte:

1. Garantir que o processo de desenvolvimento e lançamento do software DHIS 2 esteja sujeito a um plano de verificação de segurança transparente e rigoroso;
2. Por meio de uma abordagem de pesquisa-ação, a universidade busca aprender fazendo em solidariedade com os outros;
3. Esforçar-se para desenvolver, aprender e compartilhar informações e ferramentas relevantes, oportunas e úteis para promover boas práticas de segurança;
4. O acesso a toda e qualquer informação de saúde no curso de nossa prática será regido por acordo estrito e mútuo;
5. Usar as ações da universidade para fornecer um bom exemplo de prática de segurança.

Pode haver uma tensão entre a necessidade do sistema de saúde por dados identificáveis e o direito do paciente à privacidade. Na ausência de uma legislação clara que rege a coleta e o armazenamento de dados de identificação pessoal, existem conceitos importantes que devem ser compreendidos e promovidos pelos proprietários e implementadores do sistema. Eles incluem:

** Direito de acesso **

: O direito de acesso será definido pelos regulamentos de proteção de dados de cada país. Em termos gerais, inclui informações sobre as finalidades de processamento, as categorias de dados pessoais processados, os destinatários ou categorias de destinatários, duração do armazenamento, informações sobre os direitos do titular dos dados, como retificação, apagamento ou restrição de processamento, o direito para contestar, informações sobre a existência de um processo automatizado de tomada de decisão, incluindo definição de perfis, etc. Esteja ciente das regulamentações específicas para sua área e certifique-se de estar pronto para cumpri-la antes de começar a coletar dados.

** Direito de apagamento **

: O direito de apagamento também é definido pelos regulamentos de proteção de dados de cada país. Em termos gerais, os dados pessoais devem ser apagados imediatamente quando os dados não são mais necessários para a finalidade original de processamento ou se o titular dos dados retirou o seu consentimento e não existe outro fundamento legal para o processamento. Novamente, certifique-se de entender os regulamentos de sua área específica e certifique-se de estar pronto para cumpri-los.

** Minimização de dados **

: A ideia básica da minimização de dados é que o processamento de dados deve usar apenas os dados necessários para realizar uma determinada tarefa. Também implica que os dados coletados para uma finalidade não podem ser usados para outra finalidade que não o processamento original sem consentimento posterior.

** Pseudonimização **

: É um procedimento de gestão de dados que torna os dados pessoais menos identificáveis, mantendo-os adequados para análise e processamento. Isso pode ser feito substituindo o valor de alguns dos campos de dados por um ou mais identificadores artificiais ou pseudônimos. Dados pseudonimizados podem ser restaurados para tornar os indivíduos identificáveis novamente, enquanto dados anônimos nunca podem ser restaurados ao seu estado original. Dependendo dos regulamentos aplicáveis à sua área, você pode definir uma estratégia de pseudonimização que atenda aos regulamentos e às suas necessidades.

** Rastreabilidade **

: Para usar os dados de forma eficaz, precisamos garantir sua integridade. Para garantir sua integridade, é importante monitorar esses dados quando eles são coletados, processados e movidos. Você precisa entender: “o quê”, “quando”, “por que” e “quem”. Organizações que aproveitam a rastreabilidade são capazes de localizar dados com mais rapidez e são mais capazes de oferecer suporte aos requisitos de segurança e privacidade.

Com base nas regulamentações de seu território e na complexidade de seu projeto, incluindo o nível de risco potencial, você deve implementar medidas técnicas e organizacionais adequadas, como pseudonimização, minimização de dados, registros de auditoria, restrições de pesquisa, compartilhamento granular, etc, e integrar as salvaguardas necessárias no processamento de dados a fim de atender aos requisitos dos regulamentos que se aplicam à sua região.

Uma abordagem de segurança / privacidade adequada para qualquer implementação de DHIS2 que capture dados pessoalmente identificáveis incluiria a criação de uma política clara nomeando um indivíduo (s) com acesso total ao sistema, com a responsabilidade de garantir o seguinte. Para qualquer suporte técnico em bancos de dados contendo dados confidenciais, um NDA assinado com uma data de término clara deve ser exigido para terceiros.

|  | Possível implementação prática |
| --- | --- |
| ** Direito de acesso e direito de apagamento ** | Dar acesso ao paciente ao seu prontuário eletronicamente para sua revisão ou exclusão não está disponível no DHIS 2 (2.32). Você deve garantir que implementou outros métodos pelos quais um paciente pode solicitar uma cópia de seu registro para que possa revisá-lo e solicitar alterações ou sua exclusão. Se sua exclusão não for possível, você deve tornar o registro anônimo removendo / substituindo todos os pontos de dados identificáveis. |
| ** Minimização de dados ** | Certifique-se de que há um motivo válido para a coleta de dados pessoais identificáveis. Não colete detalhes desnecessários que não atendam a um propósito prático em termos de análise de dados ou a necessidade de finibilidade de um registro de paciente. Por exemplo, se a necessidade de acompanhamento do paciente for determinada por um resultado de teste ser positivo, não colete o nome do paciente se o resultado for negativo. |
| ** Pseudonimização ** | Considere o uso de valores alternativos para registrar informações sobre certos procedimentos ou condições de um paciente. Por exemplo, você pode ter uma lista de procedimentos médicos / comportamento pessoal / ações listadas como uma lista de cores. Isso permite fazer análises, sem revelar o que poderia ser um procedimento / ação / comportamento estigmatizado em um determinado território. |
| ** Rastreabilidade ** | O DHIS 2 fornece registro de auditoria detalhado para cada ponto de dados. Isso inclui o rastreamento de dados capturados por meio de suas ferramentas web (a partir da 2.22), bem como importados ou via Android (a partir da versão 2.27). Atualmente (2.32) o DHIS 2 não oferece uma opção de exportação de exclusão / anonimato completo, pois a exclusão de um valor preserva os dados anteriores no log de auditoria. Por esse motivo, qualquer compartilhamento de dados exportados com terceiros deve incluir a remoção manual de dados sensíveis / identificáveis. |

Para recomendações práticas sobre a configuração do DHIS 2 para garantir a proteção e segurança dos dados, leia a seção [Considerações sobre segurança e proteção de dados] (# configuration_security).
