from chaveAPI import key
import google.generativeai as genai
import PIL.Image
from time import sleep
import google.generativeai as genai

class IA():
    def __init__(self, key: str, model : str = 'gemini-1.5-flash',):
        """
        Classe para configurar e iniciar a IA usando a API do GEMINI.

        :param key: Chave da API do GEMINI.
        :param model: Modelo de IA a ser usado (padrão: 'gemini-1.5-flash').  
        """

        self.key = key  
        
        # CONFIGURAÇÕES DA IA GEMINI
        genai.configure(api_key=key)
        self.model = genai.GenerativeModel(model)
        
        # TESTA PARA VER SE A KEY E MODEL FORAM PASSADOS CORRETAMENTE
        try:
            response = self.model.generate_content("Escreva apenas 'Ok, IA iniciada!' se tudo estiver funcionando!")
            print(response.text)
        except Exception as e:
            print(e)
            print("Erro ao iniciar a chave da API")
            return
        
        # INICIA O HISTORICO DO CHAT BOT PARA PODER SER USADO NA FUNCAO
        self.chat = self.model.start_chat(history=[])


    def roteiroChatBotAdvanced(self, roteiro : str = '', resetRoteiro = False):
        """
        Define o roteiro do chatBotAdvanced, além de poder resetá-lo

        :param roteiro: Define o roteiro da IA.
        :param resetRoteiro: Apaga o Roteiro Atual, pode ser usado junto com um 'novo roteiro'
        """

        # RESETA O ROTEIRO E CHAT
        if resetRoteiro == True:
            self.chat = self.model.start_chat(history=[])

        # DEFINE SE A IA TERÁ UM ROTEIRO 
        self.roteiro = roteiro
        roteiro = 'Qualquer instrução que for passada, siga a risca! Seja educada e direta ao ponto!'
        if self.roteiro != '':
            roteiro = self.roteiro
        
        # DEFINE O ROTEIRO DA IA 
        self.chat.send_message(roteiro)


    def chatBotAdvanced(self, input : str = '', printResponse : bool = False):
        """
        Inicia uma conversa com o chatBot que mantém histórico

        :param input: Mensagem a ser enviada na converda com a ia
        :param printResponse: Define se a função retornará o texto ou apenas imprimirá no terminal
        """
        
        # ENVIA A MENSAGEM PARA O CHAT E ARMAZENA NO HISTORICO
        response = self.chat.send_message(input)

        # DEFINE SE A FUNÇÃO RETORNARÁ O TEXTO OU IMPRIMIRÁ NO TERMINAL
        if printResponse == True:
            print(response.text)
        else:
            return(response.text)
        
    
    def audio_image_txt(self, pathAudio: str = '', printResponse : bool = False):
        """
        
        """
        arquivo = genai.upload_file(pathAudio)

        result = self.model.generate_content([arquivo, "descreva esse arquivo, em português! Se for uma imagem, descreva de forma simplificada!"])

        if printResponse == True:
            print(result.text)
        else:
            return(result.text)
      
        arquivo.delete()

if __name__ == "__main__":
    ia = IA(key=key)
    
    # ia.roteiroChatBotAdvanced(roteiro= 'Seja um italiano com sotaque e mal educado, puxe assunto comigo, tenha resposta de no max 20 palavras',)

    # ia.chatBotAdvanced(input='É verdade que você é o naruto? eu sou o Sasuke?',
    #             printResponse=True)
   
    ia.audio_image_txt(pathAudio='image.png', printResponse=True)