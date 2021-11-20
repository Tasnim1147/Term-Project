    def findValidRookSq(self): # Changes the color of valid squares into green
        posOfRook = roundTuple(self.piece.getPos())
        self.squares[posOfRook].setColor(0, 1, 0)
        x = posOfRook[0]
        y = posOfRook[1]
        z = posOfRook[2]
        validSq = []
#         print(posOfRook)
#         print(x, y, z)
        for i in range(1, 9): # going positive x axis
            a = x + i
            potentialSq = (a, y, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 9):# going neg x axis
            a = x - i
            potentialSq = (a, y, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 9):# going positive y axis
            a = y + i
            potentialSq = (x, a, z)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 9):# going neg y axis
            a = y - i
            potentialSq = (x, a, z)
            if self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 3):# going positive z axis
            a = z + i
            b = y + (i * 8)
            potentialSq = (x, b, a)
            print(potentialSq)
            if self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq)and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 3):# going neg z axis
            a = z - i
            b = y - (i * 8)
            potentialSq = (x, b, a)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
                
        for i in range(1, 3): # Upper level rights
            a = x + i
            b = y + (8 * i)
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
                
        for i in range(1, 3): # Upper level lefts
            a = x - i
            b = y + (8 * i)
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 3): # lower level lefts
            a = x - i
            b = y - (8 * i)
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 3): # lower level lefts
            a = x + i
            b = y - (8 * i)
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 3):# Upper level ups
            a = x  
            b = y + (8 * i) + i
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 3): # lower level down
            a = x 
            b = y - (8 * i) - i
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 3): # upper level down
            a = x 
            b = y + (8 * i) - i
            c = z + i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        for i in range(1, 3): # lower level ups
            a = x 
            b = y - (8 * i) + i
            c = z - i
            potentialSq = (a, b, c)
            if self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                validSq += [self.pieces[potentialSq]]
            elif not self.checkFreeSq(potentialSq) and potentialSq in self.squares:
                if roundTuple(self.pieces[potentialSq].getColor()) != self.colorOfPiece:
                    validSq += [self.pieces[potentialSq]]
                    break
                else:
                    break
        return validSq