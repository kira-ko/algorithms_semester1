import random
from lab3.task8.src.main import k_closest_points_to_origin

def generate_test_case(n, K, coord_limit=10**6):
    points = [(random.randint(-coord_limit, coord_limit), random.randint(-coord_limit, coord_limit)) for _ in range(n)]
    return points

def test_small_case():
    points = [(1, 2), (2, 2), (3, 3)]
    n, K = len(points), 2
    expected = sorted(points[:K], key=lambda p: p[0]**2 + p[1]**2)
    result = k_closest_points_to_origin(n, K, points)
    assert result == expected
    print("Test small case passed!")

def test_random_case():
    n, K = 100, 10
    points = generate_test_case(n, K)
    result = k_closest_points_to_origin(n, K, points)
    assert len(result) == K
    print("Random test case passed! Result length:", len(result))

def test_large_case():
    n, K = 10**5, 100
    points = generate_test_case(n, K, coord_limit=10**9)
    result = k_closest_points_to_origin(n, K, points)
    assert len(result) == K
    print("Large test case passed! Result length:", len(result))

if __name__ == "__main__":
    test_small_case()
    test_random_case()
    test_large_case()