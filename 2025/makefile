# Parametric Makefile for day01.cpp ... day24.cpp + common sources
# Usage:
#   make DAY=05            # release build (O3 + fast-math)
#   make DAY=05 DEBUG=1    # debug build (-O0 -g)
#   make run DAY=05
#   make gdb DAY=05
#   make clean

CXX := g++

# ---- Choose the day file to build ----
DAY ?= 0X
DAY_SRC := day$(DAY).cpp

# ---- Common sources compiled/linked alongside the day file ----
# Space-separated list; add more as needed.
COMMON_SRCS := pchrono.cpp pfile.cpp putils.cpp
# Example:
# COMMON_SRCS := pchrono.cpp utils.cpp helpers.cpp
BUILD_DIR := build
SRCS   := $(DAY_SRC) $(COMMON_SRCS)
OBJS := $(addprefix $(BUILD_DIR)/,$(SRCS:.cpp=.o))
DEPS := $(OBJS:.o=.d)
TARGET := day$(DAY)


# ---- Flags ----
STD      := -std=c++20
WARN     := -Wall -Wextra
DEPFLAGS := -MMD -MP
BASE     := $(STD) $(WARN) $(DEPFLAGS) -DDAY_NUM=$(DAY)

# Default Debug build: make DEBUG=1
CXXFLAGS := $(BASE) -O0 -g -fno-omit-frame-pointer -DDEBUG

ifeq ($(RELEASE),1)
	# Optimized build (fast)
	CXXFLAGS := $(BASE) -O3 -ffast-math -DNDEBUG -DRELEASE 
endif

# ---- Rules ----
.PHONY: all clean run gdb

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(BUILD_DIR)/%.o: %.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

run: $(TARGET)
	./$(TARGET)

# Launch GDB TUI for the selected day (forces DEBUG=1 for sane symbols)
gdb: DEBUG=1
gdb: $(TARGET)
	gdb -tui ./$(TARGET)

clean:
	rm -rf $(BUILD_DIR) day?? 

# Include auto-generated dependencies
-include $(DEPS)
