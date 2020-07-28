// nthTenlyPrime(n)
// We will say that a number is "tenly" (a made-up term) if the digits of the 
// number add up to 10. So 1153 is tenly, but 153 is not. With this in mind, write 
// the function nthTenlyPrime(n) that takes a non-negative int n and returns the 
// nth number that is both tenly and prime. You should also write all the required 
// helper functions. The first several tenly primes are: 19, 37, 73, 109, 127…

class nthtenlyprime {
	public int fun_nthtenlyprime(int n) {
        int count = 0;
        int tenlyPrime = 19;

        while (count <= n) {
            tenlyPrime += 2;

            if (sumOfDigits(tenlyPrime) == 10 && isPrime(tenlyPrime)) {
                count++;
            }
        }
		return tenlyPrime;
    }
    
    public int sumOfDigits(int n) {
        int sum = 0;

        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }

        if (n == 2 || n == 3) {
            return true;
        }

        for (int i = 2; i < n / 2; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}