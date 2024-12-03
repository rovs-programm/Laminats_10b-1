def aprekinat_laminatu(plaksnes_garums, plaksnes_platums, istabas_garums, istabas_platums):
    kopejas_plaksnes = 0
    atlikusais_platums = istabas_platums
    rindas_numurs = 1

    while atlikusais_platums > 0:
        rindas_plaksnes = 0
        rindas_garums = istabas_garums

        if rindas_numurs % 2 == 1:
            # Nepāra rinda
            while rindas_garums > 0:
                rindas_plaksnes += 1
                rindas_garums -= plaksnes_garums
        else:
            # Pāra rinda
            rindas_plaksnes += 0.5
            rindas_garums -= plaksnes_garums / 2
            while rindas_garums > 0:
                rindas_plaksnes += 1
                rindas_garums -= plaksnes_garums

        kopejas_plaksnes += rindas_plaksnes
        atlikusais_platums -= plaksnes_platums
        rindas_numurs += 1

    return kopejas_plaksnes

# pārbaude

plaksnes_platums = float(input("Ievadiet plāksnes platumu (m): "))
istabas_garums = float(input("Ievadiet istabas garumu (m): "))
istabas_platums = float(input("Ievadiet istabas platumu (m): "))
pakas_cena = float(input("Ievadiet lamināta pakas cenu (EUR): "))
pakas_platiba = float(input("Ievadiet pakas platību (m²): "))
plaksnes_garums = float(input("Ievadiet plāksnes garumu (m): "))

