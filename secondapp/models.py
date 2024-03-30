from django.db import models


class Coin(models.Model):
    side = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_last_n_flip(n: int):
        result = {'орел': 0, 'решка': 0}
        flips = Coin.objects.order_by('-timestamp')[n:]
        for flip in flips:
            if flip.side == 'орел':
                result['орел'] += 1
            else:
                result['решка'] += 1
        return result
