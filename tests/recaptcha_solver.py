import os
import random, time


### TOOL TO DELAY #######################################
def delay(frequency: str = ''):                         #
    frequency.lower()                                   #
    # frequency : ['low', 'nice', 'high']               #
    if frequency:                                       #
        timein: int = 0                                 #
        if frequency == 'low':                          #
            timein = time.sleep(random.randint(6, 11))  #
        elif frequency == 'nice':                       #
            timein = time.sleep(random.randint(9, 14))  #
        elif frequency == 'high':                       #
            timein = time.sleep(random.randint(12, 17)) #
        else:                                           #
            timein = time.sleep(random.randint(2, 4))   #
        return timein                                   #
#########################################################


class CaptchaSolver:
    
    def __init__(self, driver):
        
        # webdriver manager
        self.driver = driver
        
        # pastas para audios ReCaptcha
        self.audio_path = os.path.join(os.getcwd(), 'audios')
        if not os.path.exists(self.audio_path):
            os.makedirs(self.audio_path)

        """
            Objeto com muitas etapas, para uma mulhor manutencão e mantimento
            do código aplicar uma chamada em pilha vinculada ao valor de  índice
            em uma chamada do objeto com protocolo iterador (loop).
        """
        
        self.steps: list = (
            self.acess_captcha_frame,
            self.click_checkbox_captcha,
            self.switch_to_audio_frame,
            self.download_audio,
            self.recogonize_audio,
            self.submit_response
        )
    
    def __iter__(self):
        # RETORNAR OBJETO COMO ITERADOR
        self.__idx: int = 0
        return self
    
    def __next__(self):
        # buscando posicão índice de qual etapa
        if self.__idx >= len(self.steps):
            # Se indice for maior que o tamanho da etapada, todas tarefas foram conclúidas
            raise StopIteration
        else:
            # Buscando qual etapa se encontra o objeto
            step = self.steps[self.__idx]
            self.__idx += 1
            return step()  # chamando o objeto como funcão

    def __call__(self):
        # Na chamada do objeto como funcãoo execute de forma assíncrona cada tarefa/etapa
        event = asyncio.get_event_loop()
        task = event.create_task(self.mainloop())

        event.run_until_complete(task)

        awaitable = asyncio.all_tasks(loop=event)
        for task in awaitable:
            task.cancel()

        gather = asyncio.gather(*awaitable, return_exeptions=True)
        event.run_until_complete(gather)
        event.close()

    async def mainloop(self):
        for step in self:
            pass  # Executa cada tarefa automaticamente ao chamar o iterador


    #############################################################################
    #       PRINCIPAIS ETAPAS MÉTODOS EXECUTADOS DENTRO DO ITERADOR             #
    #############################################################################
    def acess_captcha_frame(self):
        print("## INFO ##: ACESSANDO FRAME DO `ReCaptcha`")
        delay('nice')
    
    def click_checkbox_captcha(self):
        print("## INFO ##: CLICANDO CHECKBOX RECAPTCHA")
        delay('low')
    
    def switch_to_audio_frame(self):
        print("## INFO ##: BUSCANDO FRAME DE CAPTCHA AUDIO")
        delay()

        print("##INFO ##: ATIVANDO DESAFIO DE ÁUDIO")
        delay()
    
    def download_audio(self):
        print("## INFO ##: BAIXANDO ARQUIVO DE AUDIO")
        delay('high')
        xaudio = '** AQUI VAI TER A FONTE DO AUDIO **'
        print("## INFO ##: FONTE ÁUDIO[%s]" % xaudio)
    
    def recogonize_audio(self):
        delay()
        xkey_captcha = '** AQUI O AUDIO TRADUZIDO **'
        print("## INFO ##: Código ReCaptcha %s" % xkey_captcha)
    
    def submit_response(self):
        print("## INFO ##: ENVIANDO RESPOSTA DO RECAPTCHA")
        delay('low')


if __name__ == '__main__':
    solver = CaptchaSolver('teste_driver')
    for steps in solver:
        pass