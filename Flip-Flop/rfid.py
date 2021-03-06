#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import time
import RPi.GPIO as GPIO
import MFRC522
import faapRasp
 
# UID dos cartões que possuem acesso liberado.
CARTOES_LIBERADOS = {
    '65:74:3:AB:B9': 'Luciane',
    'F308CABD4': 'Alessandro',
    '4F:FD:2F:0:9D': 'FilipeFlop',
    '3C:2F:4F:0:2D': 'Teste',
}
 
try:
    # Inicia o módulo RC522.
    LeitorRFID = MFRC522.MFRC522()
 
    print('Aproxime seu cartão RFID')
 
    while True:
        # Verifica se existe uma tag próxima do módulo.
        status, tag_type = LeitorRFID.MFRC522_Request(LeitorRFID.PICC_REQIDL)
 
        if status == LeitorRFID.MI_OK:
            print('Cartão detectado!')
 
            # Efetua leitura do UID do cartão.
            status, uid = LeitorRFID.MFRC522_Anticoll()
 
            if status == LeitorRFID.MI_OK:
                #uid = ':'.join(['%X' % x for x in uid])
		uid = ''.join(['%X' % x for x in uid])
                print('UID do cartão: %s' % uid)
 
                # Se o cartão está liberado exibe mensagem de boas vindas.
                if uid in CARTOES_LIBERADOS:
                    print('Acesso Liberado!')
                    print('Olá %s.' % CARTOES_LIBERADOS[uid])
		    faapRasp.sendDataBluemix(uid)
                else:
                    print('Acesso Negado!')
 
                print('Aproxime seu cartão RFID')
 
        time.sleep(.25)
except KeyboardInterrupt:
    # Se o usuário precionar Ctrl + C
    # encerra o programa.
    GPIO.cleanup()
    print('nPrograma encerrado.')
