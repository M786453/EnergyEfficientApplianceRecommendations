import { Box, Grid, Image, Text, Badge, VStack } from '@chakra-ui/react';

interface Product {
  id: number;
  name: string;
  description: string;
  image: string;
  price: number;
  availability: boolean;
  power: string;
  voltage: string;
}

const dummyProducts: Product[] = [
  {
    id: 1,
    name: 'Smart Refrigerator',
    description: 'Energy-efficient smart fridge with touchscreen',
    image: 'https://example.com/fridge.jpg',
    price: 1299.99,
    availability: true,
    power: '150W',
    voltage: '110V',
  },
  {
    id: 3,
    name: 'Smart Washing Machine',
    description: 'Wi-Fi enabled washer with multiple wash cycles',
    image: 'https://example.com/washer.jpg',
    price: 899.99,
    availability: true,
    power: '1200W',
    voltage: '220V',
  },
  {
    id: 4,
    name: 'Air Purifier',
    description: 'HEPA filter air purifier with air quality sensor',
    image: 'https://example.com/airpurifier.jpg',
    price: 299.99,
    availability: false,
    power: '60W',
    voltage: '110V',
  },
  {
    id: 5,
    name: 'Smart Oven',
    description: 'Convection oven with smartphone control',
    image: 'https://example.com/oven.jpg',
    price: 749.99,
    availability: true,
    power: '1800W',
    voltage: '220V',
  },
  {
    id: 6,
    name: 'Robot Mop',
    description: 'Automated mopping robot with mapping technology',
    image: 'https://example.com/robotmop.jpg',
    price: 349.99,
    availability: true,
    power: '40W',
    voltage: '110V',
  }
];

export default function Products() {
  return (
    <Box maxWidth="1200px" margin="auto" mt={8}>
      <Grid templateColumns="repeat(auto-fill, minmax(250px, 1fr))" gap={6}>
        {dummyProducts.map((product) => (
          <Box key={product.id} borderWidth="1px" borderRadius="lg" overflow="hidden">
            <Image src={product.image} alt={product.name} />
            <Box p="6">
              <VStack align="start" spacing={2}>
                <Text fontWeight="bold" fontSize="xl">
                  {product.name}
                </Text>
                <Text>{product.description}</Text>
                <Text fontWeight="bold" color="blue.500">
                  ${product.price.toFixed(2)}
                </Text>
                <Badge colorScheme={product.availability ? 'green' : 'red'}>
                  {product.availability ? 'In Stock' : 'Out of Stock'}
                </Badge>
                <Text>Power: {product.power}</Text>
                <Text>Voltage: {product.voltage}</Text>
              </VStack>
            </Box>
          </Box>
        ))}
      </Grid>
    </Box>
  );
}