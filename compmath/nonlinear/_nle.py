from compmath._base import BasicSolver
from compmath.nonlinear import bin_search, newton_method, chord_method, simple_iteration


class NLESolver(BasicSolver):
    def __init__(
            self,
            criterion='abs_deviation',
            eps=1e-6,
            max_iter=100
    ):
        super().__init__(criterion, eps, max_iter)

        self.method_to_func = {
            'bin_search': bin_search,
            'newton_method': newton_method,
            'chord_method': chord_method,
            'simple_iteration': simple_iteration
        }

    def solve(self, **kwargs):
        func = kwargs['f']
        method = kwargs['method']
        a = kwargs['a']
        b = kwargs['b']

        if method == 'simple_iteration':
            phi = kwargs['phi']
            return simple_iteration(phi, func, a, b, eps=self.eps)

        return self.method_to_func[method](func, a, b, eps=self.eps)


