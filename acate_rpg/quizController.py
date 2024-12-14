from quizView import QuizView
from cursoView import CursoView
from cursoDAO import CursoDAO
from personagemController import PersonagemController
from quiz import Quiz
import time


class QuizController():
    def __init__(self):

        self.__quizrh = {
    "1": {
        "a": "Aumentar o número de funcionários",
        "b": "Desenvolver e gerir talentos na organização",
        "c": "Reduzir os custos operacionais",
        "pergunta": "Qual é o principal objetivo da gestão de recursos humanos?",
        "resposta": "b"
    },
    "2": {
        "a": "Contratar candidatos externos",
        "b": "Promover funcionários atuais para novas posições",
        "c": "Realizar entrevistas com pessoas de fora da empresa",
        "pergunta": "O que é recrutamento interno?",
        "resposta": "b"
    },
    "3": {
        "a": "Aumento de salário",
        "b": "Rotatividade de funcionários",
        "c": "Recrutamento de novos colaboradores",
        "pergunta": "O que significa 'turnover' em RH?",
        "resposta": "b"
    },
    "4": {
        "a": "Ajudar na contratação de novos funcionários",
        "b": "Implementar e avaliar programas de treinamento",
        "c": "Monitorar o cumprimento de normas de segurança",
        "pergunta": "Qual é a principal função de um analista de treinamento e desenvolvimento?",
        "resposta": "b"
    },
    "5": {
        "a": "Marketing voltado para consumidores",
        "b": "Estratégia para engajar os funcionários dentro da empresa",
        "c": "Aumentar as vendas por meio de campanhas internas",
        "pergunta": "O que significa 'endomarketing'?",
        "resposta": "b"
    },
    "6": {
        "a": "Reduz o tempo de contratação",
        "b": "Traz novas ideias e diversidade para a empresa",
        "c": "Evita a necessidade de treinamento",
        "pergunta": "Qual é a vantagem do recrutamento externo?",
        "resposta": "b"
    },
    "7": {
        "a": "Medir o nível de satisfação do cliente",
        "b": "Analisar o desempenho dos funcionários em relação às suas metas",
        "c": "Avaliar a qualidade dos produtos da empresa",
        "pergunta": "O que é a avaliação de desempenho?",
        "resposta": "b"
    },
    "8": {
        "a": "Lista de promoções automáticas para funcionários",
        "b": "Estrutura de progressão profissional dentro da empresa",
        "c": "Um curso oferecido para novos funcionários",
        "pergunta": "O que é plano de carreira?",
        "resposta": "b"
    },
    "9": {
        "a": "Que os funcionários recebam bônus",
        "b": "Que a empresa esteja em conformidade com as regulamentações trabalhistas",
        "c": "Que todos os funcionários tenham seguro de saúde",
        "pergunta": "O que o departamento de RH deve garantir em relação às leis trabalhistas?",
        "resposta": "b"
    },
    "10": {
        "a": "Benefícios fixos para todos os funcionários",
        "b": "Benefícios que podem ser personalizados de acordo com as necessidades dos funcionários",
        "c": "Um plano de cortes de benefícios para reduzir custos",
        "pergunta": "O que é uma política de benefícios flexíveis?",
        "resposta": "b"
    },
    "11": {
        "a": "Apenas comunicar a demissão ao funcionário",
        "b": "Oferecer suporte e realizar o desligamento de maneira correta e respeitosa",
        "c": "Realizar o pagamento imediato das verbas rescisórias",
        "pergunta": "Qual é a função do RH em uma demissão?",
        "resposta": "b"
    },
    "12": {
        "a": "Processo de alternância de turnos",
        "b": "Rotação de funcionários entre diferentes funções ou departamentos",
        "c": "Sistema de avaliação de desempenho",
        "pergunta": "O que é 'job rotation'?",
        "resposta": "b"
    },
    "13": {
        "a": "Que o novo colaborador conheça o ambiente e as políticas da empresa",
        "b": "Que o colaborador inicie imediatamente suas atividades sem treinamento",
        "c": "Que o colaborador participe de entrevistas com seus colegas",
        "pergunta": "O que o RH deve garantir na integração de novos colaboradores?",
        "resposta": "a"
    },
    "14": {
        "a": "Condições físicas do ambiente de trabalho",
        "b": "Percepção dos funcionários sobre o ambiente e cultura da empresa",
        "c": "Temperatura média nos escritórios",
        "pergunta": "O que é clima organizacional?",
        "resposta": "b"
    },
    "15": {
        "a": "Avaliação das competências técnicas do candidato",
        "b": "Avaliação de como o candidato reage em situações específicas",
        "c": "Perguntas sobre a vida pessoal do candidato",
        "pergunta": "O que é uma entrevista comportamental?",
        "resposta": "b"
    },
    "16": {
        "a": "Avaliar funcionários apenas por resultados numéricos",
        "b": "Focar no desenvolvimento das habilidades necessárias para o cargo",
        "c": "Treinar apenas os funcionários novos",
        "pergunta": "O que é gestão por competências?",
        "resposta": "b"
    },
    "17": {
        "a": "Habilidades técnicas adquiridas ao longo da carreira",
        "b": "Competências comportamentais e emocionais, como comunicação e trabalho em equipe",
        "c": "Habilidades manuais específicas para o trabalho",
        "pergunta": "O que são soft skills?",
        "resposta": "b"
    },
    "18": {
        "a": "Aconselhamento sobre questões pessoais",
        "b": "Processo de orientação para desenvolver o potencial dos funcionários",
        "c": "Recrutamento de novos talentos",
        "pergunta": "O que significa 'coaching' no contexto de RH?",
        "resposta": "b"
    },
    "19": {
        "a": "Garantir que todos os funcionários tenham os mesmos benefícios",
        "b": "Promover políticas e práticas que incentivem a diversidade e inclusão na empresa",
        "c": "Aumentar a quantidade de benefícios para minorias",
        "pergunta": "Qual é o papel do RH na diversidade e inclusão?",
        "resposta": "b"
    },
    "20": {
        "a": "Avaliação do funcionário feita apenas por seu supervisor direto",
        "b": "Avaliação feita pelo funcionário, colegas, subordinados e supervisores",
        "c": "Feedback dado em reuniões semanais",
        "pergunta": "O que é feedback 360 graus?",
        "resposta": "b"
    }
}

        self.__quizfinanceiro = {
    "1": {
        "a": "Planejar o crescimento da empresa",
        "b": "Controlar receitas e despesas",
        "c": "Realizar auditorias fiscais",
        "pergunta": "Qual é a principal função do setor financeiro?",
        "resposta": "b"
    },
    "2": {
        "a": "Fluxo de caixa",
        "b": "Orçamento de capital",
        "c": "Relatório de sustentabilidade",
        "pergunta": "Qual ferramenta financeira projeta entradas e saídas de dinheiro?",
        "resposta": "a"
    },
    "3": {
        "a": "Aumentar as vendas",
        "b": "Reduzir o custo dos produtos",
        "c": "Maximizar o valor para os acionistas",
        "pergunta": "Qual é o objetivo principal de uma empresa em termos financeiros?",
        "resposta": "c"
    },
    "4": {
        "a": "Investimento em ações",
        "b": "Controle do orçamento",
        "c": "Gestão do passivo",
        "pergunta": "Qual é uma das principais atividades da tesouraria em uma empresa?",
        "resposta": "a"
    },
    "5": {
        "a": "Lançamento de ações",
        "b": "Captação de recursos",
        "c": "Gerenciamento de caixa",
        "pergunta": "O que envolve a emissão de títulos de dívida corporativa?",
        "resposta": "b"
    },
    "6": {
        "a": "Dinheiro necessário para operações diárias",
        "b": "Recursos destinados à expansão",
        "c": "Reservas para pagamento de impostos",
        "pergunta": "O que significa 'capital de giro'?",
        "resposta": "a"
    },
    "7": {
        "a": "Registro de ações",
        "b": "Relatório financeiro anual",
        "c": "Demonstração do resultado",
        "pergunta": "Qual documento demonstra a lucratividade de uma empresa?",
        "resposta": "c"
    },
    "8": {
        "a": "Auditoria externa",
        "b": "Projeção de vendas",
        "c": "Previsão de fluxo de caixa",
        "pergunta": "Qual ferramenta ajuda a prever as necessidades futuras de caixa de uma empresa?",
        "resposta": "c"
    },
    "9": {
        "a": "Depreciação",
        "b": "Amortização",
        "c": "Desvalorização cambial",
        "pergunta": "Qual termo descreve a redução do valor de um ativo ao longo do tempo?",
        "resposta": "a"
    },
    "10": {
        "a": "Análise SWOT",
        "b": "Análise de liquidez",
        "c": "Análise de alavancagem",
        "pergunta": "Qual métrica mede a capacidade de uma empresa de pagar suas dívidas de curto prazo?",
        "resposta": "b"
    },
    "11": {
        "a": "Valor presente líquido",
        "b": "Taxa interna de retorno",
        "c": "Margem bruta",
        "pergunta": "Qual método é utilizado para avaliar o retorno de um investimento?",
        "resposta": "a"
    },
    "12": {
        "a": "Auditoria interna",
        "b": "Controle de estoques",
        "c": "Gestão de riscos",
        "pergunta": "Qual departamento é responsável pela prevenção de fraudes financeiras?",
        "resposta": "a"
    },
    "13": {
        "a": "Pagamentos a fornecedores",
        "b": "Provisão de garantias bancárias",
        "c": "Gestão de custos indiretos",
        "pergunta": "Qual é uma função básica do contas a pagar?",
        "resposta": "a"
    },
    "14": {
        "a": "Taxa de crescimento sustentável",
        "b": "Margem de lucro operacional",
        "c": "Faturamento bruto",
        "pergunta": "Qual indicador mede a eficiência da operação de uma empresa?",
        "resposta": "b"
    },
    "15": {
        "a": "Análise horizontal",
        "b": "Análise de cenários",
        "c": "Análise vertical",
        "pergunta": "Qual técnica compara itens de demonstrações financeiras ao longo do tempo?",
        "resposta": "a"
    },
    "16": {
        "a": "Déficit financeiro",
        "b": "Superávit de caixa",
        "c": "Endividamento total",
        "pergunta": "Qual termo indica quando as receitas excedem as despesas?",
        "resposta": "b"
    },
    "17": {
        "a": "Empréstimo bancário",
        "b": "Crédito rotativo",
        "c": "Captação de capital de terceiros",
        "pergunta": "Qual é uma forma de financiamento de curto prazo?",
        "resposta": "b"
    },
    "18": {
        "a": "Índice de solvência",
        "b": "Índice de liquidez corrente",
        "c": "Índice de giro do ativo",
        "pergunta": "Qual índice mede a capacidade de uma empresa em cumprir suas obrigações de longo prazo?",
        "resposta": "a"
    },
    "19": {
        "a": "Distribuição de dividendos",
        "b": "Liquidação de dívidas",
        "c": "Captação de recursos via IPO",
        "pergunta": "O que ocorre quando uma empresa decide pagar seus acionistas?",
        "resposta": "a"
    },
    "20": {
        "a": "Capital de terceiros",
        "b": "Empréstimo interbancário",
        "c": "Reserva de lucros",
        "pergunta": "Qual termo refere-se ao dinheiro emprestado por uma empresa?",
        "resposta": "a"
    }
}
        self.__quizmarketing = {
    "1": {
        "a": "Divulgar produtos ou serviços",
        "b": "Criar embalagens de produtos",
        "c": "Gerenciar os recursos financeiros",
        "pergunta": "Qual é o principal objetivo do marketing?",
        "resposta": "a"
    },
    "2": {
        "a": "Aumentar a produção",
        "b": "Criar valor para o cliente",
        "c": "Desenvolver estratégias de vendas",
        "pergunta": "Qual é a função central de uma estratégia de marketing?",
        "resposta": "b"
    },
    "3": {
        "a": "Pesquisa de mercado",
        "b": "Auditoria financeira",
        "c": "Gestão de pessoas",
        "pergunta": "Qual ferramenta é usada para entender as necessidades do consumidor?",
        "resposta": "a"
    },
    "4": {
        "a": "Propor melhorias no produto",
        "b": "Aumentar o engajamento nas redes sociais",
        "c": "Identificar oportunidades de mercado",
        "pergunta": "O que é o papel da pesquisa de mercado?",
        "resposta": "c"
    },
    "5": {
        "a": "Monitoramento do ROI de campanhas",
        "b": "Controle de estoque",
        "c": "Análise de custos de produção",
        "pergunta": "O que o marketing de desempenho visa medir?",
        "resposta": "a"
    },
    "6": {
        "a": "Analisar o mercado",
        "b": "Aumentar o número de funcionários",
        "c": "Gerenciar a cadeia de suprimentos",
        "pergunta": "Qual é uma responsabilidade do gerente de marketing?",
        "resposta": "a"
    },
    "7": {
        "a": "Estratégia de distribuição de produtos",
        "b": "Planejamento de marketing",
        "c": "Definição de metas financeiras",
        "pergunta": "Qual é a função do plano de marketing?",
        "resposta": "b"
    },
    "8": {
        "a": "Gestão de marca",
        "b": "Controle de qualidade",
        "c": "Gerenciamento de vendas",
        "pergunta": "Qual é a principal função do branding?",
        "resposta": "a"
    },
    "9": {
        "a": "Analisar a concorrência",
        "b": "Aumentar a produção",
        "c": "Gerar leads",
        "pergunta": "Qual é o objetivo da análise de concorrência?",
        "resposta": "a"
    },
    "10": {
        "a": "Criar uma imagem positiva da marca",
        "b": "Gerenciar a logística de produtos",
        "c": "Controlar a qualidade dos produtos",
        "pergunta": "Qual é o principal objetivo das relações públicas?",
        "resposta": "a"
    },
    "11": {
        "a": "Oferecer um desconto",
        "b": "Aumentar o engajamento e interações",
        "c": "Vender diretamente ao cliente",
        "pergunta": "Qual é o objetivo do marketing de conteúdo?",
        "resposta": "b"
    },
    "12": {
        "a": "Alinhar produto e preço",
        "b": "Definir preço baseado na demanda",
        "c": "Criar campanhas para fidelizar clientes",
        "pergunta": "Qual é a função da precificação baseada em valor?",
        "resposta": "b"
    },
    "13": {
        "a": "Reduzir custos operacionais",
        "b": "Promover o produto de forma criativa",
        "c": "Controlar a produção em massa",
        "pergunta": "Qual é o papel da propaganda no mix de marketing?",
        "resposta": "b"
    },
    "14": {
        "a": "Segmentar o público-alvo",
        "b": "Definir metas de crescimento",
        "c": "Gerenciar a distribuição do produto",
        "pergunta": "Qual é a primeira etapa em uma campanha de marketing?",
        "resposta": "a"
    },
    "15": {
        "a": "Maximizar o lucro",
        "b": "Satisfazer necessidades dos consumidores",
        "c": "Reduzir o tempo de produção",
        "pergunta": "Qual é o objetivo principal de uma estratégia de posicionamento de marca?",
        "resposta": "b"
    },
    "16": {
        "a": "Aumentar as vendas",
        "b": "Promover a sustentabilidade",
        "c": "Gerar leads e oportunidades",
        "pergunta": "Qual é o papel do marketing digital?",
        "resposta": "c"
    },
    "17": {
        "a": "Fortalecer a reputação da marca",
        "b": "Reduzir custos de distribuição",
        "c": "Realizar auditorias periódicas",
        "pergunta": "Qual é o principal objetivo do marketing de influência?",
        "resposta": "a"
    },
    "18": {
        "a": "Monitorar as tendências de mercado",
        "b": "Reduzir custos de produção",
        "c": "Aumentar a produção interna",
        "pergunta": "Qual é uma função importante da análise de dados de marketing?",
        "resposta": "a"
    },
    "19": {
        "a": "Aumentar a percepção de valor",
        "b": "Criar novas oportunidades de emprego",
        "c": "Desenvolver novos produtos",
        "pergunta": "Qual é o objetivo do marketing emocional?",
        "resposta": "a"
    },
    "20": {
        "a": "Aumentar o volume de vendas",
        "b": "Entender as necessidades e desejos dos clientes",
        "c": "Distribuir produtos em novos mercados",
        "pergunta": "Qual é o principal foco do marketing centrado no cliente?",
        "resposta": "b"
    }
}
        self.__quizti = {
    "1": {
        "a": "Comprimir arquivos para economizar espaço",
        "b": "Estabelecer políticas de controle de acesso",
        "c": "Executar rotinas de backup automaticamente",
        "pergunta": "Qual é a função de um sistema de gestão de identidade e acesso (IAM)?",
        "resposta": "b"
    },
    "2": {
        "a": "Dividir a rede em sub-redes menores para melhorar a performance",
        "b": "Conectar dispositivos de rede em diferentes locais geográficos",
        "c": "Criar conexões seguras entre clientes e servidores",
        "pergunta": "Qual é a principal função do subnetting em redes de computadores?",
        "resposta": "a"
    },
    "3": {
        "a": "Identificar vulnerabilidades em software",
        "b": "Monitorar a integridade de arquivos no servidor",
        "c": "Verificar o tráfego de rede para padrões de ataque",
        "pergunta": "O que faz um sistema de detecção de intrusões (IDS)?",
        "resposta": "c"
    },
    "4": {
        "a": "Segurança física dos datacenters",
        "b": "Implementação de políticas de segurança de software",
        "c": "Segurança em ambientes virtualizados",
        "pergunta": "Qual é o maior desafio relacionado à segurança na computação em nuvem?",
        "resposta": "c"
    },
    "5": {
        "a": "Reduzir o tempo de resposta do sistema",
        "b": "Otimizar o uso de hardware físico",
        "c": "Segregar aplicações para evitar interferência mútua",
        "pergunta": "Qual é o principal benefício da virtualização de servidores?",
        "resposta": "b"
    },
    "6": {
        "a": "Faz uma cópia idêntica dos dados em tempo real",
        "b": "Armazena os dados em diferentes locais geográficos",
        "c": "Garante a criptografia dos dados transmitidos pela rede",
        "pergunta": "O que é a replicação de dados em ambientes de T.I.?",
        "resposta": "a"
    },
    "7": {
        "a": "Utiliza várias instâncias de um sistema operacional",
        "b": "Permite que múltiplos usuários acessem a mesma aplicação simultaneamente",
        "c": "Distribui automaticamente a carga de trabalho entre servidores",
        "pergunta": "O que é balanceamento de carga em um ambiente de servidores?",
        "resposta": "c"
    },
    "8": {
        "a": "Controlar as permissões de arquivos em redes Linux",
        "b": "Gerenciar dispositivos de armazenamento em massa",
        "c": "Automatizar a instalação de software",
        "pergunta": "Para que serve o comando 'chmod' em sistemas Linux?",
        "resposta": "a"
    },
    "9": {
        "a": "Atualiza o kernel do sistema operacional",
        "b": "Protege contra falhas de hardware",
        "c": "Monitora o desempenho dos aplicativos em tempo real",
        "pergunta": "O que faz um sistema de alta disponibilidade (HA)?",
        "resposta": "b"
    },
    "10": {
        "a": "Encaminhar pacotes de dados entre redes diferentes",
        "b": "Controlar o fluxo de dados dentro de uma rede",
        "c": "Proteger a rede de ataques distribuídos",
        "pergunta": "Qual é a função de um roteador em uma rede?",
        "resposta": "a"
    },
    "11": {
        "a": "Analisar logs de sistemas para encontrar falhas",
        "b": "Atualizar drivers de dispositivos automaticamente",
        "c": "Aplicar patches de segurança em servidores",
        "pergunta": "Qual é a função do software de gerenciamento de vulnerabilidades?",
        "resposta": "c"
    },
    "12": {
        "a": "Oferecer suporte a interfaces de programação",
        "b": "Servir de intermediário para requisições entre cliente e servidor",
        "c": "Fornecer acesso remoto a aplicações",
        "pergunta": "O que é um servidor proxy reverso?",
        "resposta": "b"
    },
    "13": {
        "a": "Auditar transações financeiras em sistemas de ERP",
        "b": "Controlar o acesso a recursos compartilhados em rede",
        "c": "Monitorar o tráfego de rede em busca de padrões suspeitos",
        "pergunta": "Qual é o papel de um administrador de segurança da informação?",
        "resposta": "c"
    },
    "14": {
        "a": "Controlar o uso de recursos do sistema para evitar sobrecarga",
        "b": "Registrar atividades de usuários para fins de auditoria",
        "c": "Proteger sistemas contra malware e ataques de rede",
        "pergunta": "O que é um sistema de gerenciamento de logs?",
        "resposta": "b"
    },
    "15": {
        "a": "Prevenir acessos não autorizados a sistemas de armazenamento",
        "b": "Garantir que os dados estejam disponíveis em casos de falhas",
        "c": "Permitir que aplicações acessem bancos de dados de forma eficiente",
        "pergunta": "Qual é a função de um sistema de backup e recuperação?",
        "resposta": "b"
    },
    "16": {
        "a": "Gerenciar pacotes de dados em uma rede distribuída",
        "b": "Garantir a compatibilidade entre diferentes sistemas operacionais",
        "c": "Distribuir cópias de dados entre diversos servidores",
        "pergunta": "O que faz um sistema de replicação de dados?",
        "resposta": "c"
    },
    "17": {
        "a": "Monitorar a saúde dos sistemas e redes",
        "b": "Controlar a largura de banda utilizada pelos dispositivos",
        "c": "Registrar transações em tempo real para auditorias",
        "pergunta": "O que faz um sistema de monitoramento de rede?",
        "resposta": "a"
    },
    "18": {
        "a": "Controlar a comunicação entre os serviços e clientes de um aplicativo",
        "b": "Gerenciar permissões de arquivos no servidor",
        "c": "Criar ambientes de teste para aplicações em desenvolvimento",
        "pergunta": "Qual é a função de um load balancer em sistemas de TI?",
        "resposta": "a"
    },
    "19": {
        "a": "Proteger a rede contra ataques de negação de serviço (DDoS)",
        "b": "Evitar que dispositivos ultrapassem os limites de largura de banda",
        "c": "Gerenciar a distribuição de endereços IP dentro de uma rede",
        "pergunta": "O que faz um firewall de próxima geração (NGFW)?",
        "resposta": "a"
    },
    "20": {
        "a": "Reduzir a latência de redes distribuídas",
        "b": "Realizar a verificação de vulnerabilidades no código de aplicações",
        "c": "Fornecer acesso seguro a redes remotas",
        "pergunta": "Qual é o objetivo principal de uma VPN (Virtual Private Network)?",
        "resposta": "c"
    }
}
        self.__quizvendas = {
    "1": {
        "a": "Analisar a performance dos concorrentes",
        "b": "Identificar necessidades e desejos dos clientes",
        "c": "Desenvolver campanhas de marketing",
        "pergunta": "Qual é o principal objetivo da prospecção de vendas?",
        "resposta": "b"
    },
    "2": {
        "a": "Estratégia para fechar vendas rapidamente",
        "b": "Relação de longo prazo com o cliente",
        "c": "Focar em transações únicas e de alto valor",
        "pergunta": "O que caracteriza a abordagem de 'vendas consultivas'?",
        "resposta": "b"
    },
    "3": {
        "a": "Construir confiança com o cliente",
        "b": "Oferecer descontos imediatos para aumentar vendas",
        "c": "Encerrar rapidamente as negociações",
        "pergunta": "Qual é a principal vantagem da técnica de 'rapport' em vendas?",
        "resposta": "a"
    },
    "4": {
        "a": "Aumentar o ticket médio por cliente",
        "b": "Reduzir custos operacionais de venda",
        "c": "Focar apenas em novos clientes",
        "pergunta": "O que é 'upselling'?",
        "resposta": "a"
    },
    "5": {
        "a": "Facilitar a aquisição de novos clientes",
        "b": "Fidelizar os clientes existentes",
        "c": "Reduzir o ciclo de vendas",
        "pergunta": "Qual é o principal objetivo de uma estratégia de retenção de clientes?",
        "resposta": "b"
    },
    "6": {
        "a": "Oferecer produtos complementares",
        "b": "Realizar vendas cruzadas entre setores",
        "c": "Reduzir o ciclo de vendas",
        "pergunta": "O que significa 'cross-selling' em vendas?",
        "resposta": "a"
    },
    "7": {
        "a": "Oferecer várias opções para o cliente escolher",
        "b": "Personalizar a abordagem de vendas com base no comportamento do cliente",
        "c": "Utilizar sempre a mesma estratégia de vendas",
        "pergunta": "Qual é a importância da personalização no processo de vendas?",
        "resposta": "b"
    },
    "8": {
        "a": "Oferecer descontos para atrair novos clientes",
        "b": "Prever vendas futuras com base em dados históricos",
        "c": "Focar em vendas de curto prazo",
        "pergunta": "O que é 'previsão de vendas'?",
        "resposta": "b"
    },
    "9": {
        "a": "Clientes que compram esporadicamente",
        "b": "Clientes que recomendam a marca para outras pessoas",
        "c": "Clientes que apenas usam cupons de desconto",
        "pergunta": "O que são 'clientes promotores'?",
        "resposta": "b"
    },
    "10": {
        "a": "Negociação em uma única reunião",
        "b": "Relacionamento contínuo com base na confiança",
        "c": "Fechamento de venda focado no produto",
        "pergunta": "O que caracteriza a venda baseada em relacionamento?",
        "resposta": "b"
    },
    "11": {
        "a": "Oferecer mais produtos durante o atendimento ao cliente",
        "b": "Estabelecer metas de curto prazo para fechar vendas",
        "c": "Concentrar-se em vendas imediatas ao invés de fidelização",
        "pergunta": "Qual é o foco de uma estratégia de 'venda agressiva'?",
        "resposta": "c"
    },
    "12": {
        "a": "Registrar dados de clientes para campanhas futuras",
        "b": "Estabelecer parâmetros para o atendimento ao cliente",
        "c": "Focar em prospectos que já demonstraram interesse",
        "pergunta": "O que é 'lead scoring' no processo de vendas?",
        "resposta": "c"
    },
    "13": {
        "a": "Proporcionar uma experiência única ao cliente",
        "b": "Manter contato regular para novas oportunidades de venda",
        "c": "Finalizar a venda e encerrar o contato com o cliente",
        "pergunta": "Qual é o papel do 'follow-up' no processo de vendas?",
        "resposta": "b"
    },
    "14": {
        "a": "Desenvolver argumentos de venda baseados em dados concretos",
        "b": "Oferecer descontos progressivos com o aumento do volume",
        "c": "Diminuir o tempo entre o primeiro contato e a venda",
        "pergunta": "O que caracteriza a técnica de 'proposta de valor'?",
        "resposta": "a"
    },
    "15": {
        "a": "Segmentar o público de acordo com o comportamento de compra",
        "b": "Oferecer um produto mais caro do que o inicialmente desejado",
        "c": "Estender o ciclo de vendas para maiores negociações",
        "pergunta": "Qual é o principal foco da técnica de 'qualificação de leads'?",
        "resposta": "a"
    },
    "16": {
        "a": "Concentrar-se em resolver uma objeção do cliente",
        "b": "Oferecer um desconto imediato para finalizar a venda",
        "c": "Fechar a venda mesmo sem resolver todas as objeções",
        "pergunta": "Qual é o objetivo principal de lidar com objeções em vendas?",
        "resposta": "a"
    },
    "17": {
        "a": "Vender com base nas características técnicas do produto",
        "b": "Focar nos benefícios e valor que o produto traz ao cliente",
        "c": "Vender apenas para clientes que procuram preços baixos",
        "pergunta": "O que é uma abordagem de venda focada em benefícios?",
        "resposta": "b"
    },
    "18": {
        "a": "Segmentação demográfica e geográfica de clientes",
        "b": "Fechamento de venda baseado em demonstrações técnicas",
        "c": "Uso de dados e métricas para otimizar a performance de vendas",
        "pergunta": "O que caracteriza a 'venda baseada em dados'?",
        "resposta": "c"
    },
    "19": {
        "a": "Construção de uma relação de confiança antes de propor a venda",
        "b": "Fornecer múltiplas alternativas de produtos para o cliente escolher",
        "c": "Oferecer soluções sem customização ao cliente",
        "pergunta": "Qual é o princípio central da 'venda consultiva'?",
        "resposta": "a"
    },
    "20": {
        "a": "Foco na retenção de clientes antigos",
        "b": "Abertura de novos mercados e segmentos",
        "c": "Aumentar o volume de vendas por cliente",
        "pergunta": "Qual é o principal objetivo de uma estratégia de 'market share'?",
        "resposta": "b"
    }
}
        self.__personagemController = PersonagemController()
        self.__quizView = QuizView()
        self.__cursoView = CursoView()
        self.__cursoDAO = CursoDAO()
        
    def realizar_quiz(self, personagem, cursos):
        curso_selecionado = self.__cursoView.mostra_cursos(cursos)

        if curso_selecionado == None:
            return None, None

        if curso_selecionado:
            curso_encontrado = False

            for index, curso in enumerate(cursos):
                if curso["nome"] == curso_selecionado:
                    curso_encontrado = True
                    setor = curso["setor"]
                    dificuldade = curso["dificuldade"]
                    experiencia = curso["xp_ganho"]
                    nivel_requerido = curso["nivel_requerido"]

                    if curso["realizado"]:
                        self.__cursoView.mostra_mensagem("Você já tem o certificado desse curso, esqueceu?")
                        time.sleep(2)
                        return None, None

                    if nivel_requerido > personagem.nivel:
                        self.__cursoView.mostra_mensagem("Você não tem nível suficiente para fazer esse curso, volte mais tarde!")
                        time.sleep(2)
                        return None, None

                    quiz = Quiz(setor, dificuldade)

                    perguntas = getattr(self, f"_QuizController__quiz{setor.lower()}", None)
                    if perguntas is None:
                        self.__cursoView.mostra_mensagem(f"Setor {setor} não encontrado. Não há perguntas disponíveis para este curso.")
                        time.sleep(2)
                        return None, None
                    if perguntas:
                        resultado = self.__quizView.comeca_quiz(dificuldade, setor, perguntas)
                        quiz.gabaritou_miga = resultado  

                        if resultado:
                            self.__personagemController.ganhar_experiencia(personagem, experiencia)
                            self.__personagemController.atualizar_personagem(personagem)
                            self.__cursoDAO.update(curso)
                            self.__cursoView.mostra_mensagem(f"Parabéns! Você completou o curso {curso['nome']}!")

                        else:
                            cursos[index]["realizado"] = False

                    return resultado

            if not curso_encontrado:
                self.__cursoView.mostra_mensagem("O curso selecionado não existe, tente novamente!")



        


        

            

           
       