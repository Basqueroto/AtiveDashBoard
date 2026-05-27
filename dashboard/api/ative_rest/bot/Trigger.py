class Trigger:
    def evaluate(self, ma_fast, ma_slow):
        """Recebe as médias já calculadas e decide o estado (comprar ou vender)"""
        if ma_fast is None or ma_slow is None:
            return "AGUARDAR"

        if ma_fast > ma_slow:
            return "COMPRAR"
        else:
            return "VENDER"