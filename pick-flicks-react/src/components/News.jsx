import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Grid, Row, Col, Image, Button } from 'react-bootstrap';
import './News.css';

export default class News extends Component {
    render() {
        return (
            <div>
                <Image src="assets/movie-header.jpg" className="header-image"/>
                <Grid>
                    <h2>News</h2>
                    <Row>
                        <Col xs={12} sm={8} className="main-section">
                            <p>There's no news.</p>
                        </Col>
                        <Col xs={12} sm={4} className="sidebar-section">
                            <Image src="assets/dog-people.jpg"/>
                            <p>Sorry no news...</p>
                        </Col>
                    </Row>
                </Grid>
            </div>
        )
    }
}