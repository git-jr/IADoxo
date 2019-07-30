# -*-coding:utf8;-*-

from LoadAndroid import Load
from Chatbot import Chatbot
from util import Voz
from util import Log

voz = Voz()
log = Log()
load = Load()
chatbor = Chatbot()

infos = load.carregarInformacoesIniciais()

modo_texto_ativo = False
aprender = True


def iniciar():
    if not modo_texto_ativo:
        voz.fale(load.iniciar(infos))  # Verificando nome e primeiro acesso
    else:
        load.iniciar(infos)


def receber_entrada():
    if not modo_texto_ativo:
        entrada_recebida = (voz.escute())
    else:
        entrada_recebida = input(str("%s: " % load.nomeUsu))

    return entrada_recebida


def responder(entrada):
    saida = chatbor.interagir(entrada, log.listar())

    if not modo_texto_ativo:
        voz.fale(saida[0])
    print(load.nomeUsu, ": ", entrada)
    print(load.nomeIa, ": ", saida[0])

    log.reg(entrada, saida[0])  # Registra log

    if not saida[1] and aprender:  # Cadastra uma resposta se não existir
        if not modo_texto_ativo:
            chatbor.aprender1(entrada)
        else:
            chatbor.aprenderTxt1(entrada)


iniciar()
# A função inciar tem o objetivo de garantiro regsitro do usuário se esse for a primerira vez que o app está rodando
# Se não for a primeira vez, faz uma saudação comum (bom dia, boa tarde....)

while True:
    responder(receber_entrada())
    # A resposta que o usuário receberá seja por voz ou texto deriva da entrada que o usuário fornecer
    # O clico de escuta/ responde se mantém a menos que o usuário diga algum comando de saída como "sair",
    # comandos como repodução de música que colocam o app em espera ou pare o emulador QPython manualmente.

