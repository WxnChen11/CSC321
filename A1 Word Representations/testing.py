import cPickle
data = cPickle.load(open('data.pk', 'rb'))

for i in range(10):
    v = data['vocab']
    a,b,c = data['train_inputs'].tolist()[i]
    print(v[a], v[b], v[c])