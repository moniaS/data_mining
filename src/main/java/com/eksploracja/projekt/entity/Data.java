package com.eksploracja.projekt.entity;

import javax.persistence.Entity;
import javax.persistence.Id;
import java.time.LocalDate;
import java.time.LocalTime;

@Entity
public class Data {
    @Id
    private int id;
    private String host;
    private LocalDate date;
    private LocalTime time;
    private String method;
    private String page;
    private String protocol;
    private int status;
    private int size;
}
