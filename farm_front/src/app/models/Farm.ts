import { Owner } from './Owner'
export interface Farm {
  name: string
  geometry: any
  area: number
  centroid: number[]
  municipality: string
  state: string
  creation_date: Date
  owner: Owner
}
