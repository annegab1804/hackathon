V = {0 : [1,3], 1 : [0,2,4], 2: [1,5], 3: [0,4,6], 4: [3,1,5,6], 5: [2,4,8], 6:[3,7], 7: [6,4,8], 8:[7,5]} #matrice modélisant le graphe

D = {"123456780": 0} #dictionnaire donnant la distance minimale d'une configuration

def distance(M):
    if M == "123456780":
        return 0
    else:
        if M not in D.keys():
            i=0
            L=list(M) # on transforme le mot en liste
            while L[i] != "0":
                i=i+1 #on a la position de notre 0
            d = float("inf")
            for v in V[i]:
                L2 = L.copy()
                L2[i] , L2[v] = L[v], "0"
                M2 = "".join(L2)
                print(M2)
                try: 
                    dd = distance(M2)
                    if dd< d:
                        d = dd
                except RecursionError as e:
                    continue 
            D[M] = d +1
        return D[M]



print(distance("123456780"))

#cet algorithme ne fonction par car dès que la distance est supérieure à 2 il doit faire des appels récursifs trop nombreux qui dépassent la capacité de python