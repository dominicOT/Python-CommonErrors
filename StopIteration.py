#Dominic Oladapo-Tonade - 6469

class printNum:
    def __iter__(self):
        self.x = 4
        return self

    def __next__(self):
        if self.x <= 36:        #printing the value on the console till the value reaches 36
            d = self.x
            self.x += 4
            return d
        else:
            raise StopIteration     #raising the stopiteration exception once the value gets increased from 36

obj = printNum()
value_passed = iter(obj)


for i in value_passed:
    print(i)
