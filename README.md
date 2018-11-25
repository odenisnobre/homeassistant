Automação Residencial
===================================================

Basicamente o projeto de automação foi divido em duas etapas:
```
1) Definição dos Hardwares
2) Definição do Software de Controle
```

<h3> Definições </h3>

A ideia do projeto é desenvolver um projeto de automação residencial completo envolvendo bem o conceito de IOT.
Diferentemente de quando se fala de projetos de automação residencial que as pessoas só pensam em instalar câmeras de segunda a ideia de iot é 'conectar tudo com todos' onde se pode haver a interação entre vários componente. Partindo desta ideia foi dado inicio aos estudos.

Durante os estudos de para o projeto de automação residencial foi visto que havia vários hardware o primeiro dele foi o Arduino https://www.arduino.cc/en/Main/Products. Esse se demonstrou muito eficiente mas a parte de interação gráfica levaria a um desenvolvimento muito longo e não seria algo que daria para aproveitar para outros usuários, mesmo disponibilizando o código fonte.

Passando para outros testes foi encontrado dispostivios da Broadlink http://www.ibroadlink.com/sp3/ e os demais modelos. Essas tomadas seriam de grande utilizade para poder fazer automações e criação de cenas mas isso dependeria do aplicativo próprio da tomada o que não permitia a integração/automação entre outros hardwares.

Após buscas na internet encontrei um o Sonoff https://www.itead.cc/sonoff-wifi-wireless-switch.html o que tive a impressão que seria meu hardware principal pelo baixo custo. Mas apresentava o mesmo problema dos demais hardwares que foi encontrado no mercado: se tivesse três hardwares de diferentes fabricantes seria necessários três aplicativos o que tornaria inviável o projeto de automação residencial.

Então depois de um tempo buscando algo interessantes na Internet encontrei um vídeo o youtube https://www.youtube.com/watch?v=diTQ3M5zH-0 que resolveria todos os meus problemas:

Conheci o Home Assistant: https://home-assistant.io/

Depois de um tempo lendo a sobre o Home Assistant deu pra perceber que a plataforma era excelente que além de 'resolver meus problemas' com od dispositivos era Open Source(que maravilha!!! :)), baseando na Web e desenvolvido em Python. Deu pra perceber que o Home Assistant trabalha com componentes que nada mais é do que plataforma para dispostivos ou serviços que são possíveis a integração entre eles o que se torna muito flexível o processo de integração e automação.

Bem, depois de ter encontrado o Home Assistant a próxima definição seria: Onde rodar este sistema?

Como já tinha um experiência de algum tempo com o Raspberry Pi(desde a versão 1) https://www.raspberrypi.org/products/ e já tinha aproximadamente 3 unidadas em casa optei usá-lo, a versão utilizada foi igual a esta https://produto.mercadolivre.com.br/MLB-697674443-raspberry-pi-modelo-b-plus-512mb-4-usb-arm1176jzf-s-700mhz-_JM. Além de ter em casa o preço é bem em conta pelo potencial que e ele e a entrega que ele proporciona.

<h3> Passos com o Raspberry PI </h3>

Existem vários sistemas operacionais para o Raspberry e disponível para download https://www.raspberrypi.org/downloads/ mas resolvi instar o Raspbian que, conforme informei antes, já tinha tido mais contato anteriormente.

Depois de instalado o Raspbian dava início a instalação do Home Assistant.
A instalação do Home Assistant é bem complicada tem que seguir os passos corretamente.

Para instalação pelo site oficial do HA só seguir o link https://home-assistant.io/getting-started/.

No meu caso eu segui os passos do link do youtube https://www.youtube.com/watch?v=GjzOXkPb7XE&t=329s, com os seguintes passos:

logado no raspberry, abra o terminal e execute os comandos:
* sudo raspi-config
* sudo apt-get update
* sudo apt-get upgrade
* sudo reboot
* sudo pip3 install homeassistant
* sudo nano /etc/init.d/hass-daemon, copy the script, change user to root
* sudo chmod +x /etc/init.d/hass-daemon
* sudo update-rc.d hass-daemon defaults
* sudo service hass-daemon install
* sudo reboot

Com isso, no meu caso, o sistema subiu e funcionou normalmente.

<h3> Configurações do Home Assistant </h3>

Após a instalação do sistemas chegou a hora de configurar os componentes/serviços:

O Home Assistant possui componente específicos para sua plataforma e alguns configurados são:

Os componentes principais estnão configurados no arquivo https://github.com/dedynobre/homeassistant/blob/master/configuration.yaml

<h3> Hardwares Utilizados </h3>

Os hardwares utilizados no meu projetos são:

<ul> <a href="https://pt.aliexpress.com/item/US-Plug-Orvibo-S25US-Smart-WiFi-Socket-Plug-APP-Remote-Control-US-Standard-Switch-Work/32826373664.html?spm=a2g03.search0104.3.83.sd6V1s&ws_ab_test=searchweb0_0,searchweb201602_3_10152_10065_10151_10344_10068_10345_5000017_10342_10547_10343_51102_10340_10341_5060017_10548_5130017_10541_10084_10083_10307_10539_10312_10059_5080017_10313_10314_10534_100031_10604_10603_10103_10605_10594_10596_10142_10107,searchweb201603_31,ppcSwitch_5&algo_expid=dba8bf2f-8bad-429e-a403-fb72e89ed34a-13&algo_pvid=dba8bf2f-8bad-429e-a403-fb72e89ed34a&rmStoreLevelAB=0"> Tomada Orvibo</a> - 1 Unidade </ul>

<ul> <a href="https://pt.aliexpress.com/item/Original-Broadlink-SP-Mini-3-Contros-CC-Wireless-Smart-Power-Plug-Socket-Wifi-Voice-Remote-Control/32813351231.html?spm=a2g03.search0104.3.3.1tDK3g&ws_ab_test=searchweb0_0,searchweb201602_3_10152_10065_5000015_10151_10344_10068_10345_10342_10547_10343_51102_10340_10341_10548_5130015_10541_10084_10083_10307_10539_5080015_10312_10059_10313_10314_10534_100031_10604_10603_10103_10605_10594_5060015_10596_10142_10107,searchweb201603_31,ppcSwitch_5&algo_expid=2093aa2c-ecd7-4a57-9f99-30a8cf5636c8-0&algo_pvid=2093aa2c-ecd7-4a57-9f99-30a8cf5636c8&rmStoreLevelAB=0"> Tomada Broadlink SP Mini</a> - 5 Unidades </ul> 

<ul> <a href="https://pt.aliexpress.com/item/Original-Broadlink-MP1-Socket-Plug-Remote-Control-Separately-Controllable-WiFi-4-Outlet-Power-Strip-For-Smart/32809313955.html?spm=a2g03.search0104.3.3.ko9aVm&ws_ab_test=searchweb0_0,searchweb201602_3_10152_10065_10151_10344_10068_10345_5000017_10342_10547_10343_51102_10340_10341_5060017_10548_5130017_10541_10084_10083_10307_10539_10312_10059_5080017_10313_10314_10534_100031_10604_10603_10103_10605_10594_10596_10142_10107,searchweb201603_31,ppcSwitch_5&algo_expid=6e1cda15-8ab0-472e-bc34-a49065d67392-0&algo_pvid=6e1cda15-8ab0-472e-bc34-a49065d67392&rmStoreLevelAB=0"> Tomada Broadlink MP1</a> - 2 Unidades </ul> 

<ul> <a href="https://pt.aliexpress.com/item/Broadlink-RM2-RM-PRO-Smart-Home-Automation-WiFi-IR-RF-Universal-Intelligent-Wireless-remote-Controller-for/32729931353.html?spm=a2g03.search0104.3.75.rbStcA&ws_ab_test=searchweb0_0,searchweb201602_3_10152_10065_5000015_10151_10344_10068_10345_10342_10547_10343_51102_10340_10341_10548_5130015_10541_10084_10083_10307_10539_5080015_10312_10059_10313_10314_10534_100031_10604_10603_10103_10605_10594_5060015_10596_10142_10107,searchweb201603_31,ppcSwitch_5&algo_expid=04326a10-6ca8-458e-84bf-dce5aeab441b-11&algo_pvid=04326a10-6ca8-458e-84bf-dce5aeab441b&rmStoreLevelAB=0"> Tomada Broadlink RM Mini</a> - 2 Unidades </ul> 

<ul> <a href="https://pt.aliexpress.com/item/SONOFF-interruptor-Wifi-m-dulo-Interruptor-do-Rel-Sem-Fio-B-sica-Sonoff-Casa-Inteligente-Universal/32837188535.html?spm=a2g03.search0104.3.72.a5iow2&ws_ab_test=searchweb0_0%2Csearchweb201602_3_10152_10065_10151_10344_10068_10345_5000017_10342_10547_10343_51102_10340_10341_5060017_10548_5130017_10541_10084_10083_10307_10539_10312_10059_5080017_10313_10314_10534_100031_10604_10603_10103_10605_10594_10596_10142_10107%2Csearchweb201603_31%2CppcSwitch_5&algo_expid=9982e7e6-e148-4503-9454-8b44e97e1f57-9&algo_pvid=9982e7e6-e148-4503-9454-8b44e97e1f57&rmStoreLevelAB=0"> Sonoff Basic</a> - 8 Unidades </ul> 

<ul> <a href="https://pt.aliexpress.com/item/Sonoff-Dual-Home-Automation-Wireless-WiFi-Smart-Switch-10A-Smart-Switch-Module-Remote-Control/32827070046.html?spm=a2g03.search0104.3.1.5TdJnL&ws_ab_test=searchweb0_0,searchweb201602_3_10152_10065_10151_10344_10068_5000016_10345_10342_10547_10343_51102_10340_5060016_10341_10548_5130016_10541_10084_10083_10307_10539_10312_10059_10313_5080016_10314_10534_100031_10604_10603_10103_10605_10594_10596_10142_10107,searchweb201603_31,ppcSwitch_5&algo_expid=d86bc252-caa8-48a3-b0aa-857d551eb885-0&algo_pvid=d86bc252-caa8-48a3-b0aa-857d551eb885&rmStoreLevelAB=0"> Sonoff Dual</a> - 1 Unidade </ul> 

<ul> <a href="https://pt.aliexpress.com/item/Original-Aqara-Kit-Casa-Inteligente-Wi-fi-Sem-Fio-Multifuncional-Porta-de-Entrada-Da-Janela-Da/32841014026.html?spm=a2g03.search0104.3.134.UpjyN4&ws_ab_test=searchweb0_0%2Csearchweb201602_3_10152_10065_10151_10344_10068_10345_5000017_10342_10547_10343_51102_10340_10341_5060017_10548_5130017_10541_10084_10083_10307_10539_10312_10059_5080017_10313_10314_10534_100031_10604_10603_10103_10605_10594_10596_10142_10107%2Csearchweb201603_31%2CppcSwitch_5&algo_expid=1b39b40c-79bf-4b21-a611-e3e93c04b91c-16&algo_pvid=1b39b40c-79bf-4b21-a611-e3e93c04b91c&rmStoreLevelAB=0"> Kit Xiaomi</a> - 1 Unidade </ul>

Os Sonoff foram atualizados os firmware para a versão Tasmota disponivel neste link: https://github.com/arendst/Sonoff-Tasmota

<h3> Mais Detalhes </h3>

Os detalhes da configurações, automações, scripts e notificacções estão detalhadas em cada pasta com seus respectivos comentários.


<h3> Imagens </h3>

<img src="https://github.com/dedynobre/homeassistant/blob/master/media/det1.jpg"/></br>
<img src="https://github.com/dedynobre/homeassistant/blob/master/media/det2.jpg"/></br>
<img src="https://github.com/dedynobre/homeassistant/blob/master/media/det3.jpg"/></br>
<img src="https://github.com/dedynobre/homeassistant/blob/master/media/det4.jpg"/></br>
<img src="https://github.com/dedynobre/homeassistant/blob/master/media/det5.jpg"/></br>
