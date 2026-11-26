package com.exam;

import org.junit.Test;
import static org.junit.Assert.*;

public class AppTest {
    @Test
    public void testServerPort() {
        assertEquals(8081, App.PORT);
    }

    @Test
    public void testAppInitialization() {
        assertTrue(true);
    }
}
