

transition_count = {}
text = "Je m'apelle Lise"


n = len(text)
for i in range(n-1):
    duo = text[i] + text[i+1]
    if duo in transition_count.keys():
        transition_count[duo] += 1
    else :
        transition_count[duo] = 1


for k in transition_count.keys():
    transition_count[k] /= (n-1)*1.

for k,v in transition_count.items():
    print(f"key : {k} value : {v}")

# lettre_depart = "p"
# subtransition_count = {}
# for k,v in transition_count.items():
#     if k.startswith(lettre_depart):
#         subtransition_count[k] = v

