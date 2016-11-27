import {autoinject} from 'aurelia-framework';
import {HttpClient} from 'aurelia-fetch-client';
import 'fetch';

@autoinject
export class Ideas {
  public heading = 'Ideas';
  public ideas = [];

  constructor(private http: HttpClient) {
    http.configure(config => {
      config
        .useStandardConfiguration()
        .withBaseUrl('http://localhost:8000/');
    });
  }

  public activate() {
    return this.http.fetch('ideas/')
      .then(response => response.json())
      .then(ideas => this.ideas = ideas as any);
  }
}
