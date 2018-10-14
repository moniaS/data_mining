package com.eksploracja.projekt.service;

import com.eksploracja.projekt.entity.Data;
import com.eksploracja.projekt.repository.DataRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DataService {
    private final DataRepository dataRepository;

    @Autowired
    public DataService(DataRepository dataRepository) {
        this.dataRepository = dataRepository;
    }

    public List<Data> findAll() {
        return dataRepository.findAll();
    }
}
