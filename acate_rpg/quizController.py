from quiz import Quiz
from quizView import QuizView
from cursoView import CursoView

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

        self.__quizView = QuizView()
        self.__cursoView = CursoView()
        
    def realizar_quiz(self):
        self.__cursoView.mostra_cursos(self.__cursoController.cursos)
        nome_curso = self.__cursoView.seleciona_curso()
        for curso in self.__cursoController.cursos:
            if curso.nome == nome_curso:
                setor = curso.setor

        if setor == "RH":
            self.__quizView.comeca_quiz(self.__quizrh)


        





    