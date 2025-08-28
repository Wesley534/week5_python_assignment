# week5_python_assignment
# 🦸‍♂️ Superhero and 🚗 Vehicle Programs

This document explains two Python programs: **`class.py`** (Assignment 1) and **`poly.py`** (Activity 2).  
Both demonstrate **object-oriented programming (OOP)** concepts, with a focus on **minimal code** to meet the requirements.

---

## 📘 Assignment 1: Superhero Class System (`class.py`)

### 🎯 Purpose
The program creates a class hierarchy for superheroes, showcasing **OOP principles** like **inheritance, encapsulation, and polymorphism**.  
It includes a **base `Superhero` class** and a **derived `FlyingSuperhero` class**.

### 🏗️ Structure

#### 🔹 Base Class: `Superhero`
- **Attributes**:
  - `_name` and `_secret_identity`: Encapsulated (using `_` prefix) to protect sensitive data.
  - `power_level`: Public attribute for the hero's strength.
- **Constructor**: Initializes with `name`, `secret_identity`, and `power_level`.
- **Methods**:
  - `use_power()`: Returns a string describing the hero using their power.
  - `special_ability()`: A method designed for **polymorphic override**, describing the hero's fighting style.

#### 🔹 Derived Class: `FlyingSuperhero`
- Inherits from `Superhero`, adding a `flight_speed` attribute.
- Overrides `special_ability()` to describe flying, demonstrating **polymorphism**.

#### 💡 Example Usage
- Creates a `Superhero` (**Thunderbolt**) and a `FlyingSuperhero` (**Sky Guardian**).
- Calls `use_power()` and `special_ability()` to show different behaviors.

### 🌟 Key Features
- **Encapsulation**: `_name` and `_secret_identity` are protected to restrict direct access.
- **Polymorphism**: `special_ability()` behaves differently for `Superhero` and `FlyingSuperhero`.
- **Minimal Design**: Only essential attributes and methods are included, avoiding unnecessary code.

---

## 🚀 Activity 2: Vehicle Polymorphism Challenge (`poly.py`)

### 🎯 Purpose
The program demonstrates **polymorphism** using a vehicle system, where different vehicle types implement a `move()` method uniquely (e.g., a car drives, a plane flies).

### 🏗️ Structure

#### 🔹 Base Class: `Vehicle`
- **Attributes**: `name` (public, stores the vehicle's name).
- **Constructor**: Initializes with `name`.
- **Method**: `move()` is a placeholder (`pass`) for subclasses to override.

#### 🔹 Derived Class: `Car`
- Inherits from `Vehicle`.
- Implements `move()` to return a string indicating the car is driving 🚗.

#### 🔹 Derived Class: `Plane`
- Inherits from `Vehicle`.
- Implements `move()` to return a string indicating the plane is flying ✈️.

#### 💡 Example Usage
- Creates a `Car` (**Sedan**) and a `Plane` (**Jet**).
- Uses a list of vehicles to call `move()` on each, showcasing polymorphic behavior.

### 🌟 Key Features
- **Polymorphism**: The `move()` method produces different outputs based on the vehicle type (`Car` vs. `Plane`).
- **Minimal Design**: Includes only the necessary classes, attributes, and methods to demonstrate polymorphism.
- **Clarity**: Uses emojis (🚗, ✈️) for visual distinction in output.

---

## 📌 Summary
Both programs are designed to be **concise yet effective** in demonstrating **OOP concepts**:

- **`superhero.py`** focuses on **encapsulation, inheritance, and polymorphism** with a superhero theme.  
- **`vehicles.py`** highlights **polymorphism** through a simple vehicle hierarchy.  

Each program avoids unnecessary code while fulfilling the assignment requirements, with **clear example usage** to illustrate functionality.
