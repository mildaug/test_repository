INSERT INTO mokytojai (id, vardas, pavarde, specialybe, nuo_kada_dirba_metais)
VALUES
    (1, "Petras", "Petraitis", "Matematika", 2013),
    (2, "Ona", "Onaitė", "Fizika", 2012),
    (3, "Marius", "Marijus", "Biologija", 2015),
    (4, "Rasa", "Rasaitė", "Anglų kalba", 2011),
    (5, "Aurimas", "Aurimaitis", "Lietuvių kalba", 2018),
    (6, "Gintare", "Gintarėlė", "Istorija", 2020)

SELECT * FROM mokytojai WHERE specialybe = "Matematika";

SELECT vardas, pavarde, specialybe FROM mokytojai 
WHERE (2023 - nuo_kada_dirba_metais) > 8;

SELECT vardas, pavarde, specialybe FROM mokytojai 
WHERE (2023 - nuo_kada_dirba_metais) > 9;


UPDATE mokytojai SET pavarde = 'Žolienė'
WHERE vardas = 'Rasa' AND pavarde = 'Rasaitė';

DELETE FROM mokytojai WHERE id = 4;
