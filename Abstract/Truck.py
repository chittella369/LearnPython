from Abstract.Car import Car


class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'


    def stop(self):
        return 'Truck braking!'
