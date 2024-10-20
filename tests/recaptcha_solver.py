import random, time, os, asyncio


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
            Objeto com muitas etapas, para uma melhor manutencão e mantimento
            do código aplicar uma chamada em pilha vinculada ao valor de  índice
            em uma chamada do objeto com protocolo iterador em um evento loop.
        """
        
        self.steps: tuple = (
            self.acess_captcha_frame,
            self.click_checkbox_captcha,
            self.switch_to_audio_frame,
            self.download_audio,
            self.recogonize_audio,
            self.submit_response
        )
    
    def __aiter__(self):
        # RETORNAR OBJETO COMO ITERADOR ASSÍNCRONO
        self.__idx: int = 0
        return self
    
    def __call__(self):
        # UM WRAPPER PARA AS COROUTINAS DO OBJETO
        event = asyncio.new_event_loop()
        task = event.create_task(self.mainloop())

        event.run_until_complete(task)

        awaitable = asyncio.all_tasks(loop=event)
        for task in awaitable:
            task.cancel()

        gather = asyncio.gather(*awaitable)
        event.run_until_complete(gather)
        event.close()


    async def __anext__(self):
        if self.__idx >= len(self.steps):
            raise StopIteration
        else:
            # buscando posicão índice de qual etapa
            # Buscando qual etapa se encontra o objeto
            step = self.steps[self.__idx]
            self.__idx += 1
            await step()  # instânciando métodos


    async def mainloop(self):
        # CHAMANDO ITERADOR DO OBJETO
        async for step in self:
            pass
        return self.__idx

    #############################################################################
    #       PRINCIPAIS ETAPAS MÉTODOS EXECUTADOS DENTRO DO ITERADOR             #
    #############################################################################
    async def acess_captcha_frame(self):
        print("## INFO ##: ACESSANDO FRAME DO `ReCaptcha`")
        delay()
    
    async def click_checkbox_captcha(self):
        print("## INFO ##: CLICANDO CHECKBOX RECAPTCHA")
        delay()
    
    async def switch_to_audio_frame(self):
        print("## INFO ##: BUSCANDO FRAME DE CAPTCHA AUDIO")
        delay()

        print("##INFO ##: ATIVANDO DESAFIO DE ÁUDIO")
        delay()
    
    async def download_audio(self):
        print("## INFO ##: BAIXANDO ARQUIVO DE AUDIO")
        delay('high')
        xaudio = '** AQUI VAI TER A FONTE DO AUDIO **'
        print("## INFO ##: FONTE ÁUDIO[%s]" % xaudio)
    
    async def recogonize_audio(self):
        delay()
        xkey_captcha = '** AQUI O AUDIO TRADUZIDO **'
        print("## INFO ##: Código ReCaptcha %s" % xkey_captcha)
    
    async def submit_response(self):
        print("## INFO ##: ENVIANDO RESPOSTA DO RECAPTCHA")
        delay('low')


if __name__ == '__main__':
    CaptchaSolver('teste_driver')()