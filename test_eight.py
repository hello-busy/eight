#!/usr/bin/env python3
"""
Simple tests for the eight module
"""

from eight import print_eight, eight_times_table, powers_of_eight, is_multiple_of_eight, eight_ascii_art

def test_print_eight():
    """Test that print_eight returns 8"""
    assert print_eight() == 8
    print("✓ print_eight() test passed")

def test_eight_times_table():
    """Test the multiplication table generation"""
    table = eight_times_table()
    assert len(table) == 10
    assert table[0] == (1, 8)
    assert table[4] == (5, 40)
    assert table[9] == (10, 80)
    print("✓ eight_times_table() test passed")

def test_powers_of_eight():
    """Test powers of eight generation"""
    powers = powers_of_eight(3)
    assert len(powers) == 3
    assert powers[0] == (0, 1)
    assert powers[1] == (1, 8)
    assert powers[2] == (2, 64)
    print("✓ powers_of_eight() test passed")

def test_is_multiple_of_eight():
    """Test multiple checking function"""
    assert is_multiple_of_eight(8) == True
    assert is_multiple_of_eight(16) == True
    assert is_multiple_of_eight(24) == True
    assert is_multiple_of_eight(25) == False
    assert is_multiple_of_eight(7) == False
    assert is_multiple_of_eight(0) == True  # 0 is a multiple of every number
    print("✓ is_multiple_of_eight() test passed")

def test_eight_ascii_art():
    """Test ASCII art generation"""
    art = eight_ascii_art()
    assert isinstance(art, str)
    assert len(art) > 0
    assert "█" in art  # Should contain block characters
    print("✓ eight_ascii_art() test passed")

def run_all_tests():
    """Run all tests"""
    print("Running tests for eight module...")
    print("=" * 35)
    
    test_print_eight()
    test_eight_times_table()
    test_powers_of_eight()
    test_is_multiple_of_eight()
    test_eight_ascii_art()
    
    print("=" * 35)
    print("All tests passed! ✅")

if __name__ == "__main__":
    run_all_tests()