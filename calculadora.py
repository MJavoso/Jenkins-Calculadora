class Calculadora:
    def _numeros_invalidos(self, m, n):
        if isinstance(m, float) or isinstance(n, float):
            return 'Solo se admiten números enteros positivos'

        if not isinstance(m, int) or not isinstance(n, int):
            return 'Sólo se admiten números'
        if m < 0 or n < 0:
            return 'Solo se admiten números positivos'

        return False

    def sumar(self, m, n):
        mensaje_error = self._numeros_invalidos(m, n)
        if mensaje_error:
            return mensaje_error

        return m + n

    def restar(self, m, n):
        mensaje_error = self._numeros_invalidos(m, n)
        if mensaje_error:
            return mensaje_error

        return m - n

    def multiplicar(self, m, n):
        mensaje_error = self._numeros_invalidos(m, n)
        if mensaje_error:
            return mensaje_error

        return m * n

    def dividir(self, m, n):
        mensaje_error = self._numeros_invalidos(m, n)
        if mensaje_error:
            return mensaje_error

        return m // n

    def potencia(self, m, n):
        mensaje_error = self._numeros_invalidos(m, n)
        if mensaje_error:
            return mensaje_error

        return m ** n

    def raiz(self, m, n):
        mensaje_error = self._numeros_invalidos(m, n)
        if mensaje_error:
            return mensaje_error

        return int(m ** (1/n))
