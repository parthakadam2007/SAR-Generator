package com.SAR_Generator.main_service.security;


import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.stereotype.Service;

import com.SAR_Generator.main_service.models.User;
import com.SAR_Generator.main_service.repository.UserRepository;



@Service
public class UserDetailsServiceImpl implements UserDetailsService{
    
    @Autowired
    private UserRepository userRepository;


    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByEmailNative(username);
        if (user == null) {
            // throw new UsernameNotFoundException("User not found");
            System.out.println("Customer not found with email:res " + username);
            throw new UsernameNotFoundException("User not found");

        }
        return new UserDetailModel(user);
    }
}
