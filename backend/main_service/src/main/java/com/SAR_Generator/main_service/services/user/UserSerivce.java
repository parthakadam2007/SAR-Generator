package com.SAR_Generator.main_service.services.user;

import java.util.List;

import com.SAR_Generator.main_service.dto.UserDTO;

public interface UserSerivce {
    public List<UserDTO> getAllUsers();
    public UserDTO saveUser(UserDTO UserDTO);
    public UserDTO getUserById(Long id);
    public UserDTO getUserByEmail(String email);
    public UserDTO updateUser(Long id, UserDTO UserDTO);
}
