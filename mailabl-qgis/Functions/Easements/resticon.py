class veevärk: # https://www.riigiteataja.ee/akt/114092023002
    # reoveepumpla kuja https://www.riigiteataja.ee/akt/114092023002
    pumpla_1 = "10" # kui vooluhulk on kuni 10 m³/d, peab kuja olema 10 meetrit
    pumpla_2 = "20" # kui vooluhulk on üle 10 m³/d, peab kuja olema 20 meetrit
    purgimissõlm = "30"  # Purgimissõlme kuja peab olema 30 meetrit
    survetorustik_1 = "2" # alla 250 mm siseläbimõõduga torustikul 2 m
    survetorustik_2 = "2,5" # 250 mm kuni alla 500 mm siseläbimõõduga torustikul 2,5 m
    survetorustik_3 = "3" # 500 mm ja suurema siseläbimõõduga torustikul 3 m
    vabavoolsed_torustikud_1 = "2" # siseläbimõõt on alla 250 mm ja mis on paigaldatud kuni 2 m sügavusele, – 2 m
    vabavoolsed_torustikud_2 = "2,5" # siseläbimõõt on alla 250 mm ja mis on paigaldatud sügavamale kui 2 m, – 2,5 m
    vabavoolsed_torustikud_3 = "2,5" # siseläbimõõt on 250 mm ja suurem ning mis on paigaldatud kuni 2 m sügavusele, – 2,5 m
    vabavoolsed_torustikud_4 = "3" # siseläbimõõt on 250 kuni siseläbimõõduni, mis jääb alla 1000 mm, ning mis on paigaldatud sügavamale kui 2 m, – 3 m
    vabavoolsed_torustikud_5 = "5" # siseläbimõõt on 1000 mm ja suurem ning mis on paigaldatud sügavamale kui 2 m või allmaakaeveõõnesse, – 5 m
class elekter: # https://www.riigiteataja.ee/akt/12962378 
    elekter_1 = "2" # kuni 1 kV pingega liinide korral 2 meetrit
    elekter_2 = "3" # 1 kuni 20 kV pingega liinidel õhukaabli kasutamise korral 3 meetrit
    elekter_3 = "10" # 1 kuni 20 kV pingega liinide korral 10 meetrit
    elekter_4 = "25" # 35–110 kV pingega liinide korral 25 meetrit
    elekter_5 = "40" # 220–330 kV pingega liinide korral 40 meetrit
class kaugküte: # https://www.riigiteataja.ee/akt/103022022020
    maa_alused_soojustorustikud_1 = "2" # alla 200 mm läbimõõduga torustiku korral 2 meetrit
    maa_alused_soojustorustikud_2 = "3" # 200 mm ja suurema läbimõõduga torustiku korral 3 meetrit
    maapealsed_soojustorustikud = "10" # aurutorustikul töörõhul üle 16 baari on 10 meetrit
    maapealsed_soojustorustikud = "5" # aurutorustikul töörõhul 16 baari ja alla selle on 5 meetrit
    maapealsed_soojustorustikud = "5" # veetorustikul töörõhul üle 6 baari on 5 meetrit
    maapealsed_soojustorustikud = "2" # veetorustikul töörõhul 6 baari ja alla selle on 2 meetrit
    Vedelkütusetorustik = "5" # torustiku välisseina äärmistest punktidest 5 meetrit
class gaasitorustik: # https://www.riigiteataja.ee/akt/103022022020
    gaasitorustik_1 = "1" # A- ja B-kategooria gaasipaigaldiste korral torustiku välimisest mõõtmest 1 meetrit
    gaasitorustik_2 = "2" # C-kategooria gaasipaigaldise korral torustiku välimisest mõõtmest 2 meetrit
    gaasitorustik_3 = "3" # D-kategooria gaasipaigaldise nimiläbimõõduga <200 mm torustiku korral torustiku keskjoonest 3 meetrit
    gaasitorustik_4 = "5" # D-kategooria gaasipaigaldise nimiläbimõõduga ≥200 mm ja <500 mm torustiku korral torustiku keskjoonest 5 meetrit
    gaasitorustik_5 = "10" # D-kategooria gaasipaigaldise nimiläbimõõduga ≥500 mm torustiku korral torustiku keskjoonest 10 meetrit
class sideehitis: # https://www.riigiteataja.ee/akt/103022022020
    sideehitis_maismaal = "1" # maismaal – 1 meeter sideehitisest või sideehitise välisseinast sideehitisega paralleelse mõttelise jooneni või tõmmitsatega raadiomasti korral 1 meeter välimiste tõmmitsate vundamendi välisservast ühendades tõmmitsad mõtteliseks kolmnurgaks, vabalt seisva masti korral 1 meeter vundamendi välisservast
    sideehitis_siseveekogudel = "100" # 100 meetrit sideehitise keskjoonest
    sideehitis_merel = "0,25" # 0,25 meremiili sideehitise keskjoonest