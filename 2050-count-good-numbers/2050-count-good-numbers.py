class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        number_of_odd_index = n//2
        number_of_even_index = n - number_of_odd_index
        mod = 10**9 + 7

        # # Recursion 
        # def power(base, exponent):
        #     if exponent == 1: return base
        #     if exponent == 0: return 1

        #     result = (power(base, exponent//2) % mod)
            
        #     return (result * result * base) % mod if exponent % 2 == 1 else result * result

        # answer = (power(5,number_of_even_index) % mod) * (power(4,number_of_odd_index) % mod)

        # Square-and-Multiply Algorithm(Binary Exponentiation) -> modular exponentiation
        def modular_exponentiation(base, exponent,mod):
            result = 1
            base = base % mod

            while exponent > 0:

                if exponent % 2 == 1:

                    result = (base * result) % mod

                base = (base * base) % mod

                exponent //= 2
            
            return result

            
        answer = modular_exponentiation(5,number_of_even_index,mod) * \
                modular_exponentiation(4,number_of_odd_index,mod)

        return answer% mod

        