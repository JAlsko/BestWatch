import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Jumbotron, Grid, Row, Col, Image, Button } from 'react-bootstrap';
import './About.css';

export default class About extends Component {
    render() {
        return (
            <div>
                <Image src="assets/movie-header.jpg" className="header-image"/>
                <Grid>
                    <Col xs={12} sm={8} smOffset={2}>
                        <Image src="assets/person-1.jpg" className="about-profile-pic" rounded/>
                        <h3> Frank the guy </h3>
                        <p> What a jerk, huh? </p>
                    </Col>
                </Grid>
            </div>
        )
    }
}