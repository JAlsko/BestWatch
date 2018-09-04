import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Jumbotron, Grid, Row, Col, Image, Button } from 'react-bootstrap';
import './Home.css';

export default class Home extends Component {
    render() {
        return (
            <div>
                <Image src="assets/movie-header.jpg" className="header-image"/>
                <Grid>
                    <Row className="show-grid text-center">
                        <Col xs={12} sm={3} className="movie-wrapper">
                            <h1>Audience Fave</h1>
                            <Image src="assets/movie-1.jpg" rounded className="movie-poster"/>
                            <h3>Dodgeball</h3>
                            <p>The greatest dodgeball movie ever.</p>
                        </Col>
                        <Col xs={12} sm={6} className="movie-wrapper">
                            <h1>Critics' Pick</h1>
                            <Image src="assets/movie-2.jpg" rounded className="movie-poster"/>
                            <h3>Dumb and Dumber</h3>
                            <p>Best movie about two dummies.</p>
                        </Col>
                        <Col xs={12} sm={3} className="movie-wrapper">
                            <h1>Blockbuster Hit</h1>
                            <Image src="assets/movie-3.jpg" rounded className="movie-poster"/>
                            <h3>The Wicker Man</h3>
                            <p>What's in there, a shark?</p>
                        </Col>
                    </Row>
                </Grid>
            </div>
        )
    }
}