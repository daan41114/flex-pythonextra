import io

bestand = open('test.txt','w')
bestand.write('test 123!');
bestand.close()

bestand2 = open('test.txt','r')
inhoud = bestand2.read()
print('de inhoud van het bestand is')
print(inhoud)

