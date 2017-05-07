#-*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from jnius import autoclass, cast
from kivy.clock import Clock, mainthread
from plyer import gps
import json

latx = ''
longx = ''


class Main(BoxLayout):
    def sendData(self):
        if self.ids['umaxsemana-01'].active == True:
            self.dorme_rua_entrevistado = '1 dia por semana'
        elif self.ids['duasxsemana-01'].active == True:
            self.dorme_rua_entrevistado = '2 dias por semana'
        elif self.ids['tresxsemana-01'].active == True:
            self.dorme_rua_entrevistado = '3 dias por semana'
        else:
            self.dorme_rua_entrevistado = 'Semana toda'

        if self.ids['umaxsemana-02'].active == True:
            self.dorme_albergue_entrevistado = '1 dia por semana'
        elif self.ids['duasxsemana-02'].active == True:
            self.dorme_albergue_entrevistado = '2 dias por semana'
        elif self.ids['tresxsemana-02'].active == True:
            self.dorme_albergue_entrevistado = '3 dias por semana'
        else:
            self.dorme_albergue_entrevistado = 'Semana toda'

        if self.ids['umaxsemana-03'].active == True:
            self.dorme_domicilio_entrevistado = '1 dia por semana'
        elif self.ids['duasxsemana-03'].active == True:
            self.dorme_domicilio_entrevistado = '2 dias por semana'
        elif self.ids['tresxsemana-03'].active == True:
            self.dorme_domicilio_entrevistado = '3 dias por semana'
        else:
            self.dorme_domicilio_entrevistado = 'Semana toda'

        if self.ids['umaxsemana-04'].active == True:
            self.dorme_outro_entrevistado = '1 dia por semana'
        elif self.ids['duasxsemana-04'].active == True:
            self.dorme_outro_entrevistado = '2 dias por semana'
        elif self.ids['tresxsemana-04'].active == True:
            self.dorme_outro_entrevistado = '3 dias por semana'
        else:
            self.dorme_outro_entrevistado = 'Semana toda'

        if self.ids['faz_ganha_dinheiro1'].active == True:
            self.faz_ganha_dinheiro = 'Construção civil'
        elif self.ids['faz_ganha_dinheiro2'].active == True:
            self.faz_ganha_dinheiro = 'Guardador de carro / flanelinha'
        elif self.ids['faz_ganha_dinheiro3'].active == True:
            self.faz_ganha_dinheiro = 'Carregador/ estivador'
        elif self.ids['faz_ganha_dinheiro4'].active == True:
            self.faz_ganha_dinheiro = 'Catador de material reciclável'
        elif self.ids['faz_ganha_dinheiro5'].active == True:
            self.faz_ganha_dinheiro = 'Serviços gerais/ limpeza/ outro'
        elif self.ids['faz_ganha_dinheiro6'].active == True:
            self.faz_ganha_dinheiro = 'Pede dinheiro'
        elif self.ids['faz_ganha_dinheiro7'].active == True:
            self.faz_ganha_dinheiro = 'Vendas'
        elif self.ids['faz_ganha_dinheiro8'].active == True:
            self.faz_ganha_dinheiro = 'Outro'
        else:
            self.faz_ganha_dinheiro = 'Não respondeu'


        self.uf_origem = self.ids.uf_origem.text
        self.municipio_origem = self.ids.municipio_origem.text
        self.localizacao = "POINT(" + str(self.longitude) + " " + str(self.latitude) + ")"
        self.entrevistador_nome = self.ids.entrevistador_nome.text
        self.cpf = self.ids.cpf.text
        self.observacoes = self.ids.observacoes.text
        self.respostas_fornecidas = self.ids.respostas_fornecidas.text
        self.nro_ordem = self.ids.nro_ordem.text
        self.nome_entrevistado = self.ids.nome_entrevistado.text
        self.apelido = self.ids.apelido.text
        self.cpf_entrevistado = self.ids.cpf_entrevistado.text
        self.rg_entrevistado = self.ids.rg_entrevistado.text
        self.rg_comple_entrevistado = self.ids.rg_comple_entrevistado.text
        self.rg_dataemi_entrevistado = self.ids.rg_dataemi_entrevistado.text
        self.rg_estadoemi_entrevistado = self.ids.rg_estadoemi_entrevistado.text
        self.sigla_emissor_rg = self.ids.sigla_emissor_rg.text
        self.nascimento_entrevistado = self.ids.nascimento_entrevistado.text
        self.grau_escolaridade_entrevistado = self.ids.grau_escolaridade_entrevistado.text
        self.tempo_vive_rua = self.ids.tempo_vive_rua.text
        self.motivo_mora_rua = self.ids.motivo_mora_rua.text
        self.tempo_mora_cidade = self.ids.tempo_mora_cidade.text
        self.vive_familia = self.ids.vive_familia.text
        self.contato_parente_fora_rua = self.ids.contato_parente_fora_rua.text
        self.frenq_ativ_comunit = self.ids.frenq_ativ_comunit.text
        self.local_atendimento = self.ids.local_atendimento.text
        self.emprego_carteira = self.ids.emprego_carteira.text

        print self.localizacao
        self.params = json.dumps(
            {
                "uf_origem": self.uf_origem if self.uf_origem else None,
                "municipio_origem": self.municipio_origem if self.municipio_origem else None,
                "localizacao": self.localizacao,
                "entrevistador_nome": self.entrevistador_nome if self.entrevistador_nome else None,
                "cpf": self.cpf if self.cpf else None,
                "observacoes": self.observacoes if self.observacoes else None,
                #"respostas_fornecidas": self.respostas_fornecidas if self.respostas_fornecidas else None --vericar
                "nro_ordem": self.nro_ordem if self.nro_ordem else None,
                "nome_entrevistado": self.nome_entrevistado if self.nome_entrevistado else None,
                "apelido": self.apelido if self.apelido else None,
                "cpf_entrevistado": self.cpf_entrevistado if self.cpf_entrevistado else None,
                "rg_entrevistado": self.rg_entrevistado if self.rg_entrevistado else None,
                "rg_comple_entrevistado": self.rg_comple_entrevistado if self.rg_comple_entrevistado else None,
                "rg_dataemi_entrevistado": self.rg_dataemi_entrevistado if self.rg_dataemi_entrevistado else None,
                "rg_estadoemi_entrevistado": self.rg_estadoemi_entrevistado if self.rg_estadoemi_entrevistado else None,
                "sigla_emissor_rg": self.sigla_emissor_rg if self.sigla_emissor_rg else None,
                "nascimento_entrevistado": self.nascimento_entrevistado if self.nascimento_entrevistado else None,
                "grau_escolaridade_entrevistado": self.grau_escolaridade_entrevistado if self.grau_escolaridade_entrevistado else None,
                "dorme_rua_entrevistado": self.dorme_rua_entrevistado if self.dorme_rua_entrevistado else None,
                "dorme_albergue_entrevistado": self.dorme_albergue_entrevistado if self.dorme_albergue_entrevistado else None,
                "dorme_domicilio_entrevistado": self.dorme_domicilio_entrevistado if self.dorme_domicilio_entrevistado else None,
                "dorme_outro_entrevistado": self.dorme_outro_entrevistado if self.dorme_outro_entrevistado else None,
                "tempo_vive_rua": self.tempo_vive_rua if self.tempo_vive_rua else None,
                "motivo_mora_rua": self.motivo_mora_rua if self.motivo_mora_rua else None,
                "tempo_mora_cidade": self.tempo_mora_cidade if self.tempo_mora_cidade else None,
                "vive_familia": self.vive_familia if self.vive_familia else None,
                "contato_parente_fora_rua": self.contato_parente_fora_rua if self.contato_parente_fora_rua else None,
                "frenq_ativ_comunit": self.frenq_ativ_comunit if self.frenq_ativ_comunit else None,
                "local_atendimento": self.local_atendimento if self.local_atendimento else None,
                "emprego_carteira": self.emprego_carteira if self.emprego_carteira else None,
                "faz_ganha_dinheiro": self.faz_ganha_dinheiro if self.faz_ganha_dinheiro else None
            }
        )
        self.headers = {'Content-type': 'application/json',
                        'Accept': 'application/json; charset=UTF-8',
                        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}

        self.req = UrlRequest('http://192.168.1.109:8000/api/add/', req_body=self.params, req_headers=self.headers,
                              on_success=self.postSucess, on_error=self.postFail)


    def postSucess(self, req, result):
        text = Label(text="Enviado com sucesso!".format())
        pop_up = Popup(title="Sucesso", content=text, size_hint=(.7, .7))
        pop_up.open()

    def postFail(self, req, result):
        text = Label(text="Erro de conexão, verifique sua internet!".format())
        pop_up = Popup(title="Erro de conexão", content=text, size_hint=(.7, .7))
        pop_up.open()


class PessoaRuaMobApp(App):
    gps_get = StringProperty()
    gps_location = StringProperty()
    gps_status = StringProperty()
    lat = NumericProperty()
    long = NumericProperty()

    def build(self):
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)
            self.start(0, 1000)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'Por favor, ative o GPS'

        return Main()


    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)


    def stop(self):
        gps.stop()


    @mainthread
    def on_location(self, **kwargs):
        self.lat = kwargs.get('lat')
        self.long = kwargs.get('lon')

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)


    def on_pause(self):
        gps.stop()
        return True


    def on_resume(self):
        gps.start(1000, 0)
        pass

if __name__ == '__main__':
    PessoaRuaMobApp().run()