def __init__(self,
             swarmsize,
             minvalues,
             maxvalues,
             currentVelocityRatio,
             localVelocityRatio,
             globalVelocityRatio):
    """
    swarmsize - размер роя (количество частиц)
    minvalues - список, задающий минимальные значения для каждой координаты частицы
    maxvalues - список, задающий максимальные значения для каждой координаты частицы
    currentVelocityRatio - общий масштабирующий коэффициент для скорости
    localVelocityRatio - коэффициент, задающий влияние лучшей точки,
найденной каждой частицей, на будущую скорость
    globalVelocityRatio - коэффициент, задающий влияние лучшей точки,
найденной всеми частицами, на будущую скорость
    """