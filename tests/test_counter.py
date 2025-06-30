from nicegui.testing import User
from nicegui import ui
import pytest


async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0"""
    await user.open('/')
    await user.should_see('Simple Counter')
    await user.should_see('0')


async def test_counter_increment(user: User) -> None:
    """Test incrementing the counter"""
    await user.open('/')
    
    # Initially should see 0
    await user.should_see('0')
    
    # Click the increment button
    user.find(marker='increment').click()
    
    # Should now see 1
    await user.should_see('1')


async def test_counter_decrement(user: User) -> None:
    """Test decrementing the counter"""
    await user.open('/')
    
    # Initially should see 0
    await user.should_see('0')
    
    # Click decrement to go negative
    user.find(marker='decrement').click()
    
    # Should now see -1
    await user.should_see('-1')


async def test_counter_multiple_operations(user: User) -> None:
    """Test multiple increment and decrement operations"""
    await user.open('/')
    
    # Start at 0
    await user.should_see('0')
    
    # Increment 3 times
    for _ in range(3):
        user.find(marker='increment').click()
    await user.should_see('3')
    
    # Decrement 2 times
    for _ in range(2):
        user.find(marker='decrement').click()
    await user.should_see('1')


async def test_counter_negative_values(user: User) -> None:
    """Test that counter can go negative"""
    await user.open('/')
    
    # Start at 0
    await user.should_see('0')
    
    # Decrement twice to go negative
    user.find(marker='decrement').click()
    await user.should_see('-1')
    
    user.find(marker='decrement').click()
    await user.should_see('-2')


async def test_counter_ui_elements_present(user: User) -> None:
    """Test that all UI elements are present"""
    await user.open('/')
    
    # Check for title
    await user.should_see('Simple Counter')
    
    # Check for buttons by their markers
    await user.should_see(marker='increment')
    await user.should_see(marker='decrement')
    
    # Check for counter display
    await user.should_see(marker='counter')


async def test_counter_button_functionality(user: User) -> None:
    """Test button functionality sequence"""
    await user.open('/')
    
    # Test increment sequence: 0 -> 1 -> 2
    await user.should_see('0')
    user.find(marker='increment').click()
    await user.should_see('1')
    user.find(marker='increment').click()
    await user.should_see('2')
    
    # Test decrement sequence: 2 -> 1 -> 0 -> -1
    user.find(marker='decrement').click()
    await user.should_see('1')
    user.find(marker='decrement').click()
    await user.should_see('0')
    user.find(marker='decrement').click()
    await user.should_see('-1')