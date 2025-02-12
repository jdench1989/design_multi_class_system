# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
Car
- 4x tyres
- readings = [
    {"timestamp": ...., 
        "front": {"left": tyre,"right": tyre},
        "rear": {"left": tyre, "right": tyre}
    }
]
- take_reading()

Tyre()
- tread_depth
- pressure


```

_Also design the interface of each class in more detail._

```python
class Car():

    def __init__(self, fl, fr, rl, rr):
        self.front_left = fl
        self.front_right = fr
        self.rear_left = rl
        self.rear_right = rr
        
    def get_latest_readings(self):
        front_left = self.front_left.get_latest_reading()
        ...
        return ({
            "Front left": front_left,
            .....
        })

class Tyre:
    
    def __init__(self):
        self.readings = []
        # => [{"timestamp": datetime.now, "pressure": xxxx, "tread_depth": xxxx]}, ...]

    def take_reading(self, pressure, tread_depth):
        # side effect: append reading with timestamp to start of self readings list
        pass

    def get_latest_reading(self):
        return self.readings[0]


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
