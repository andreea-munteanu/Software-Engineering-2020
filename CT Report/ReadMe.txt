We provide labels for training set as a simple .csv file, containing following columns (headed included):

Filename - train file name

LeftLungAffected - binary label for presence of any TB lesions in the left lung

RightLungAffected - binary label for presence of any TB lesions in the right lung

CavernsLeft - binary label for presence of caverns in the left lung

CavernsRight - binary label for presence of caverns in the right lung

PleurisyLeft - binary label for presence of pleurisy in the left lung

PleurisyRight - binary label for presence of pleurisy in the right lung

Plese note, that “presence of any TB lesions” means any TB lesions, not limited to caverns or pleurisy. So rows like “1,1,0,0,0,0” are correct.