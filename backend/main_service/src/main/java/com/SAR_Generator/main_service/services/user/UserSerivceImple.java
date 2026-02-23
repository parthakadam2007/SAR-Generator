package com.SAR_Generator.main_service.services.user;

import com.SAR_Generator.main_service.dto.UserDTO;
import com.SAR_Generator.main_service.mapper.UserMapper;
import com.SAR_Generator.main_service.models.User;
import com.SAR_Generator.main_service.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.UserDetailsManager;
import org.springframework.stereotype.Service;

@Service
public class UserSerivceImple  implements   UserSerivce {
    private UserRepository userRepository;

    private  final PasswordEncoder passwordEncoder;

    public UserSerivceImple(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public UserDTO getUserByEmail(String email){
        User user = userRepository.findByEmailNative(email);

        UserDTO userDTO = UserMapper.toDTO(user);

        return userDTO;
    }



    public UserDTO saveUser(UserDTO userDTO){
        User user = UserMapper.toEntity(userDTO);
        user.setPasswordHash(passwordEncoder.encode(user.getPasswordHash()));

        user = userRepository.save(user);
        UserDTO response = UserMapper.toDTO(user);

        return   response;
    }
}
